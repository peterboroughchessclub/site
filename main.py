# filepath: macros/main.py
import os

def define_env(env):
    @env.macro
    def gallery_images():
        # Use absolute path or check current working directory
        project_root = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(project_root, "docs", "news")
        images = []
        for img in sorted(os.listdir(img_dir)):
            if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(f'![{img}](./news/{img})')
        return "\n\n".join(images)