import unreal

unreal.log("Hello Unreal")
unreal.log_warning("Caution!")

# unreal.AssetManager.find_assets()

obj_path = "/Game/StarterContent/Blueprints/Assets/M_LightStage_Skybox_HDRI.M_LightStage_Skybox_HDRI"

reg = unreal.AssetRegistryHelpers.get_asset_registry()
'''
asset_data = reg.get_asset_by_object_path(
    object_path=obj_path,
    include_only_on_disk_assets=True
)
'''
asset_data = reg.get_asset_by_object_path(object_path=obj_path)
print(asset_data)

'''
filt = unreal.ARFilter(
    package_paths=["/Game/StarterContent/Textures"],
    class_names=["Texture2D"],
    recursive_paths=True,
    include_only_on_disk_assets=True
)

assets = reg.get_assets(filt)

# text = "Found {} assets".format(len(assets))
# "Found " + str(len(assets)) + " assets"
text = f"Found {len(assets)} assets"
unreal.log(text)
'''

