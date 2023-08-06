import json
from logging import getLogger

log = getLogger(__name__)


def validate_schema(Schema):
    def wrapper(func):
        schema = Schema()

        def handler(event, context):
            log.debug("received event: " + json.dumps(event))
            event = schema.load(event)
            return func(event, context=context)

        return handler

    return wrapper
