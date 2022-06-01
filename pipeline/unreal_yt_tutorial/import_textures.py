import unreal
from pathlib import Path

TEX_SOURCE_DIR = Path("C:\\Users\\etudiant\\Downloads\\BMRH__Pack_Textures_Photocopy-&-Grunge\\BMRH_Grunge_Texture_V1")
VALID_EXTS = (".png", ".tif", ".tiff", ".tga", ".jpg")
DEST_DIR_UE = "/Game/StarterContent/TexturesImported"
SAVE_FREQ = 5  # Save after importing every N assets
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

paths_to_import = list()
for file_path_abs in TEX_SOURCE_DIR.iterdir():
    if file_path_abs.suffix not in VALID_EXTS:
        continue
    paths_to_import.append(file_path_abs)


num_assets_to_save = 0
counter = 0
with unreal.ScopedSlowTask(len(paths_to_import), "Custom Texture Import") as slow_task:
    for file_path_abs in paths_to_import:
        if slow_task.should_cancel():
            break
        slow_task.enter_progress_frame(1)

        name = file_path_abs.stem
        file_name_parts = name.split("_")
        file_name_start = file_name_parts[1]
        only_letters = [ch for ch in file_name_start if ch.isalpha()]
        tex_category = "".join(only_letters)
        unreal.log(f"{num_assets_to_save}: {tex_category} {file_path_abs.suffix}")

        task = unreal.AssetImportTask()
        task.automated = True
        task.filename = str(file_path_abs)
        task.destination_path = f"{DEST_DIR_UE}/{tex_category}"
        task.destination_name = tex_category + str(counter)
        task.replace_existing = True
        task.save = False
        unreal.log(f"Importing {task.destination_name}")
        asset_tools.import_asset_tasks([task])

        num_assets_to_save += 1
        counter += 1
        if num_assets_to_save >= SAVE_FREQ:
            unreal.EditorLoadingAndSavingUtils.save_dirty_packages(
                save_map_packages=False,
                save_content_packages=True
            )
            num_assets_to_save = 0
