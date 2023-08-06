
import asyncio
import logging 

from ..core import base_client

logger = logging.getLogger(__name__)

class ProcessControlClient(base_client.BaseClient):

    def __init__(self, url, session=None, identity=None):
        super(ProcessControlClient, self).__init__(url, session, identity)

    async def __start_process_instance(self, process_model_id):
        path = f"/api/consumer/v1/process_models/{process_model_id}/start?startCallbackType=1"

        result = await self.do_post(path, {})

        return result

    async def __start_process_instance_by_start_event(self, process_model_id, start_event_id):
        path = f"/api/consumer/v1/process_models/{process_model_id}/start?startCallbackType=1&start_event_id={start_event_id}"

        result = await self.do_post(path, {})

        return result

    def start_process_instance(self, process_model_id, start_event_id=None):

        async def run_loop(process_model_id, start_event_id):
            result = None
            
            if start_event_id is not None:
                result = await self.__start_process_instance_by_start_event(process_model_id, start_event_id)
            else:
                result = await self.__start_process_instance(process_model_id)

            await self.close()

            return result

        logger.info(f"Starting process instance process_model_id '{process_model_id}' and start_event_id '{start_event_id}'.")

        loop = asyncio.get_event_loop()

        task = run_loop(process_model_id, start_event_id)
        result = loop.run_until_complete(task)

        loop.close()

        return result