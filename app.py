from PIL import Image
import sys
if sys.argv[0] == "img":
    import_file_path = sys.argv[1]
    im1 = Image.open(import_file_path)
    export_file_path = sys.argv[2]
    im1.save(export_file_path)