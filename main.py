import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':

    binance = BinanceClient("760f834af04f29db9ee8e3753c4b45e9eef71cf844d1f0b5f26b24bfb6786b6d",
                            "3ba60a39766432f2802e141c4373032223122dce4635a18450ada0ff13662080",
                            testnet=True, futures=True)

    bitmex = BitmexClient("5z4Rh3tn8U_eAZBs5S6vHgj0", "Q0u5gHVDDmZtC39cujvUVC4jzHPRsSziJar7JisjQs5tcCbk",
                          testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
