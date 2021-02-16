import pyvips

image = pyvips.Image.new_from_file("/Users/admin/Documents/svs/parasetamol.svs")
image.dzsave("betadin", overlap=0, tile_size=512, depth="one")
# image = pyvips.Image.new_form_file('/Users/admin/Documents/parasetamol.svs')