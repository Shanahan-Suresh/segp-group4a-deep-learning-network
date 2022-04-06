from torchvision.utils import save_image

def get_image(image):
    save_image_tensor(image)
def save_image_tensor(image_tensor):
    image_tensor = image_tensor.squeeze(0)
    image_tensor = image_tensor.swapaxes(2, 1)
    image_tensor = image_tensor.swapaxes(1, 0)
    print(image_tensor.shape)
    save_image(image_tensor,"train_image.png")

def refresh_image(preview_image):
    preview_image.setStyleSheet("image: url(train_image.png);border :1px solid black;")
