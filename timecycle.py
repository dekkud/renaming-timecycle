import re

filenames = [
    "w_blizzard.xml", "w_clear.xml", "w_clearing.xml", "w_clouds.xml",
    "w_extrasunny.xml", "w_foggy.xml", "w_halloween.xml", "w_neutral.xml",
    "w_overcast.xml", "w_rain.xml", "w_rainhalloween.xml", "w_smog.xml",
    "w_snow.xml", "w_snowhalloween.xml", "w_snowlight.xml",
    "w_thunder.xml", "w_xmas.xml"
]

source_file = "w_blizzard.xml"

with open(source_file, "r", encoding="utf-8") as f:
    original_content = f.read()

for target_file in filenames:
    name_upper = target_file.replace("w_", "").replace(".xml", "").upper()
    modified_content = re.sub(
        r'<cycle name=".*?" regions=".*?">',
        f'<cycle name="{name_upper}" regions="2">',
        original_content,
        count=1
    )
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(modified_content)
