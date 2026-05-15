import os.path
from datetime import datetime



class Screenshot:
    @staticmethod
    def capture(driver, name):
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        path = os.path.join(folder,filename)
        driver.save_screenshot(path)
        print("Taken the screenshots", path)
        # logger.info("Captured screenshot")
        # logger.info(path)
        return path
