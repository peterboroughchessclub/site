# filepath: macros/main.py
import os

def define_env(env):
    @env.macro
    def gallery_images():
        img_dir = "docs/news"
        images = []
        for img in sorted(os.listdir(img_dir)):
            if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(f'![{img}](./news/{img})')
        return "\n\n".join(images)