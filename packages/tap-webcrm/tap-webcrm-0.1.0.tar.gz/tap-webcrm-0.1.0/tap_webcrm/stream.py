import os
import pkg_resources
import json
import sys
import traceback

from typing import Dict, Any, List

import singer
from singer import utils, metadata, Transformer
from singer.catalog import Catalog

logger = singer.get_logger()


def process_stream(client, stream, state: dict, start_date):
    # mdata = metadata.to_map(stream.metadata).get((), {})
    mdata = metadata.to_map(stream.metadata)

    bookmark_property = metadata.get(mdata, (), "bookmark_property")
    generator_attr = metadata.get(mdata, (), "generator_attr")
    include_prefix = metadata.get(mdata, (), "include_prefix")

    key_properties = stream.key_properties
    stream_name = stream.tap_stream_id

    logger.info(f"[{stream_name}] streaming..")

    checkpoint = singer.get_bookmark(state, stream_name, bookmark_property)
    if checkpoint:
        logger.info(f"[{stream_name}] previous state: {checkpoint}")

    generator = getattr(client, generator_attr)

    # transformer takes the selected fields from the catalog and filters each record
    # using the metadata for each stream
    with Transformer() as transformer:
        new_checkpoint = emit_stream(
            stream,
            generator,
            bookmark_property,
            key_properties,
            checkpoint,
            transformer,
            mdata,
            include_prefix=include_prefix,
        )

    singer.write_bookmark(state, stream_name, bookmark_property, new_checkpoint)

    logger.info(f"[{stream_name}] emitting state: {state}")

    singer.write_state(state)

    logger.info(f"[{stream_name}] done")


def emit_stream(
    stream,
    stream_generator,
    bookmark_property,
    key_properties,
    checkpoint,
    transformer,
    mdata,
    exclude_fields=None,
    include_prefix=None,
):
    # load schema from disk
    schema = stream.schema.to_dict()

    stream_name = stream.tap_stream_id

    # write schema
    singer.write_schema(stream_name, schema, key_properties)

    # keep this backup in case the pull dies
    checkpoint_backup = checkpoint

    # set the most recent update to the dawn of time
    # which is also a valid checkpoint since every
    # new record will be newer than that
    most_recent_update = "0001-01-01T00:00:00+00:00"

    try:
        with singer.metrics.record_counter(stream_name) as counter:
            for record in stream_generator():
                # retrieve updatedAt field for each record
                updated_time = record[bookmark_property]

                # skip records if there was a previous checkpoint
                if checkpoint and checkpoint >= updated_time:
                    continue

                dict_record = transformer.transform(record, schema, mdata)

                # write record with extracted timestamp
                singer.write_record(
                    stream_name, dict_record, time_extracted=utils.now()
                )

                # keep track of the most recent record
                if most_recent_update < updated_time:
                    most_recent_update = updated_time

                counter.increment(1)
        return most_recent_update

     # because the documents are ordered by createdAt time
    # and not updated at, we should only save the state when
    # a complete successful run was achieved.
    # If an error occured mid-run, thereit is almost guaranteed that
    # records that have not been processed contain an UpdatedTime that is older
    # than the
    except Exception as err:
        logger.error(traceback.format_exc())
        return checkpoint_backup
