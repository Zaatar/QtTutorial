from pipeline.engine.engine import Engine
from pathlib import Path

try:
    import unreal
except:
    unreal = None

VALID_EXTENSIONS = (".png", ".tif", ".tiff", ".tga", ".jpg")
SAVE_FREQUENCY = 5
ASSET_TOOLS = unreal.AssetToolsHelpers.get_asset_tools()


class UnrealEngine(Engine):
    def __init__(self):
        self.implements = ['Import Alembic']

    def fill_paths_to_import(self, input_directory, paths_to_import_output):
        for file_path_abs in input_directory:
            if file_path_abs.suffix not in VALID_EXTENSIONS:
                continue
            paths_to_import_output.append(file_path_abs)

    def import_asset_ue(self, import_files_directory, destination_path, dcc_save_name, save_after_every_import,
                        replace_existing):
        print(f'In Import Asset UE in Unreal Engine')
        # Prepare list of paths for import into DCC
        paths_to_import = list()
        import_directory_path = Path(import_files_directory)
        # self.fill_paths_to_import(import_directory_path, paths_to_import)
        # self.fill_paths_to_import(self, import_directory_path, paths_to_import)

        for file_path_abs in import_directory_path.iterdir():
            if file_path_abs.suffix not in VALID_EXTENSIONS:
                continue
            paths_to_import.append(file_path_abs)

        # Prepare save counter which will be reset on every save and counter to be added to import name
        save_counter = 0
        name_counter = 0

        with unreal.ScopedSlowTask(len(paths_to_import), "Custom QT Import Window") as slow_task:
            for file_path_abs in paths_to_import:
                if slow_task.should_cancel():
                    break
                slow_task.enter_progress_frame(1)

                file_name_parts = file_path_abs.stem.split("_")
                file_name_start = file_name_parts[1]
                only_letters = [ch for ch in file_name_start if ch.isalpha()]
                tex_category = "".join(only_letters)
                unreal.log(f'{save_counter}: {tex_category} {file_path_abs.suffix}')

                task = unreal.AssetImportTask()
                task.automated = True
                task.filename = str(file_path_abs)
                task.destination_path = f'{destination_path}/{tex_category}'
                task.destination_name = tex_category + str(name_counter)
                task.replace_existing = replace_existing
                task.save = save_after_every_import
                unreal.log(f'Importing {task.destination_name}')
                ASSET_TOOLS.import_asset_tasks([task])

                save_counter += 1
                name_counter += 1
                if save_counter >= SAVE_FREQUENCY:
                    unreal.EditorLoadingAndSavingUtils.save_dirty_packages(
                        save_map_packages=False,
                        save_content_packages=True
                    )
                    num_assets_to_save = 0
