import numpy as np
from PIL import Image
import io
import ftplib
from datetime import datetime

class ftpUpload:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "FTP_SERVER": ("STRING", {"default": "ftp_server"}),
                "FTP_USERNAME": ("STRING", {"default": "ftp_username"}),
                "FTP_PASSWORD": ("STRING", {"default": "ftp_password"}),
                "FTP_DIRECTORY": ("STRING", {"default": "/ftp_directory"}),
                "UPLOAD": (["enable", "disable"],),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "test"
    OUTPUT_NODE = True
    CATEGORY = "HTA"

    def test(self, image, FTP_SERVER, FTP_USERNAME, FTP_PASSWORD, FTP_DIRECTORY, UPLOAD):
        image_array = image.cpu().numpy()
        image_array = np.squeeze(image_array)

        if image_array.ndim == 3 and image_array.shape[0] in {1, 3, 4}:
            image_array = np.transpose(image_array, (1, 2, 0))

        image_array = 255. * image_array
        image_array = np.clip(image_array, 0, 255).astype(np.uint8)

        img = Image.fromarray(image_array)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"{timestamp}.png"

        ftp_server = FTP_SERVER
        ftp_user = FTP_USERNAME
        ftp_password = FTP_PASSWORD
        destination_path = f'{FTP_DIRECTORY}/{filename}'

        if UPLOAD == 'enable':
            with ftplib.FTP(ftp_server, ftp_user, ftp_password) as ftp:
                ftp.storbinary(f'STOR {destination_path}', buffer)
                print(f'Image uploaded to {ftp_server}{destination_path}')

        return {}

NODE_CLASS_MAPPINGS = {
    "ftp_upload": ftpUpload
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ftp_upload": "HTA FTP Upload"
}
