from nebu.cli.extensions import neb_extension, NebExtension

@neb_extension(name='test_ext')
def test_ext():
    return NebExtension()
