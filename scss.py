import sass
import os
import sys

SOURCE_FILE = "static/css/styles.scss" 
TARGET_FILE = "static/css/styles.css"

def compile_scss():
    target_dir = os.path.dirname(TARGET_FILE)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    print(f"🎨 Compiling {SOURCE_FILE} to {TARGET_FILE}...")

    try:
        css_content = sass.compile(
            filename=SOURCE_FILE,
            output_style='compressed',
            include_paths=['static/css']
        )

        with open(TARGET_FILE, 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        print("✅ SCSS compilation complete.")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    compile_scss()
