from pipeline.engine.engine import Engine
from pathlib import Path

try:
    import unreal
except:
    unreal = None

VALID_EXTENSIONS = (".png", ".tif", ".tiff", ".tga", ".jpg", ".abc")
SAVE_FREQUENCY = 5
ASSET_TOOLS = unreal.AssetToolsHelpers.get_asset_tools()


def fill_paths_to_import(input_directory, paths_to_import_output):
    for file_path_abs in input_directory.iterdir():
        if file_path_abs.suffix not in VALID_EXTENSIONS:
            continue
        paths_to_import_output.append(file_path_abs)


def save_dirty_packages():
    unreal.EditorLoadingAndSavingUtils.save_dirty_packages(
        save_map_packages=False,
        save_content_packages=True
    )


class UnrealEngine(Engine):
    def __init__(self):
        self.implements = ['Import Alembic']

    def import_asset_ue(self, import_files_directory, destination_path, dcc_save_name, save_after_every_import,
                        replace_existing):
        print(f'In Import Asset UE in Unreal Engine')
        # Prepare list of paths for import into DCC
        paths_to_import = list()
        import_directory_path = Path(import_files_directory)
        fill_paths_to_import(import_directory_path, paths_to_import)

        # Prepare save counter which will be reset on every save and counter to be added to import name
        save_counter = 0
        name_counter = 0

        with unreal.ScopedSlowTask(len(paths_to_import), "Custom QT Import Window") as slow_task:
            for file_path_abs in paths_to_import:
                if slow_task.should_cancel():
                    break
                slow_task.enter_progress_frame(1)

                task = unreal.AssetImportTask()
                task.automated = True
                if file_path_abs.suffix == ".abc":
                    task.options = unreal.AbcImportSettings()
                    task.options.import_type = unreal.AlembicImportType.GEOMETRY_CACHE

                    task.options.material_settings = unreal.AbcMaterialSettings(create_materials=False, find_materials=True)
                    task.options.conversion_settings = unreal.AbcConversionSettings()
                    task.options.conversion_settings.rotation = [90.0, 0.0, 0.0]

                task.filename = str(file_path_abs)
                task.destination_path = f'{destination_path}/AbcImport'
                task.destination_name = dcc_save_name + str(name_counter)
                task.replace_existing = replace_existing
                task.save = save_after_every_import
                unreal.log(f'Importing {task.destination_name}')
                ASSET_TOOLS.import_asset_tasks([task])

                save_counter += 1
                name_counter += 1

                # if save counter reaches the frequency, save the current dirty files
                if save_counter >= SAVE_FREQUENCY:
                    save_dirty_packages()
                    save_counter = 0

            # if the loop is done and there are still unsaved files, save them
            if save_counter >= 1:
                save_dirty_packages()
                save_counter = 0


'''

https://forums.unrealengine.com/t/import-alembic-with-abcimportsettings-in-unreal-4-22-using-python/127546

'''
