depends = ('ITKPyBase', 'ITKMesh', 'ITKImageGradient', 'ITKImageFunction', 'ITKCommon', )
templates = (
  ('CuberilleImageToMeshFilter', 'itk::CuberilleImageToMeshFilter', 'itkCuberilleImageToMeshFilterISS2MSS2', True, 'itk::Image< signed short,2 >, itk::Mesh< signed short,2 >, itk::InterpolateImageFunction< itk::Image< signed short,2 >, double >'),
  ('CuberilleImageToMeshFilter', 'itk::CuberilleImageToMeshFilter', 'itkCuberilleImageToMeshFilterIUC2MUC2', True, 'itk::Image< unsigned char,2 >, itk::Mesh< unsigned char,2 >, itk::InterpolateImageFunction< itk::Image< unsigned char,2 >, double >'),
  ('CuberilleImageToMeshFilter', 'itk::CuberilleImageToMeshFilter', 'itkCuberilleImageToMeshFilterIUS2MUS2', True, 'itk::Image< unsigned short,2 >, itk::Mesh< unsigned short,2 >, itk::InterpolateImageFunction< itk::Image< unsigned short,2 >, double >'),
  ('CuberilleImageToMeshFilter', 'itk::CuberilleImageToMeshFilter', 'itkCuberilleImageToMeshFilterIF2MF2', True, 'itk::Image< float,2 >, itk::Mesh< float,2 >, itk::InterpolateImageFunction< itk::Image< float,2 >, double >'),
  ('CuberilleImageToMeshFilter', 'itk::CuberilleImageToMeshFilter', 'itkCuberilleImageToMeshFilterISS3MSS3', True, 'itk::Image< signed short,3 >, itk::Mesh< signed short,3 >, itk::InterpolateImageFunction< itk::Image< signed short,3 >, double >'),
  ('CuberilleImageToMeshFilter', 'itk::CuberilleImageToMeshFilter', 'itkCuberilleImageToMeshFilterIUC3MUC3', True, 'itk::Image< unsigned char,3 >, itk::Mesh< unsigned char,3 >, itk::InterpolateImageFunction< itk::Image< unsigned char,3 >, double >'),
  ('CuberilleImageToMeshFilter', 'itk::CuberilleImageToMeshFilter', 'itkCuberilleImageToMeshFilterIUS3MUS3', True, 'itk::Image< unsigned short,3 >, itk::Mesh< unsigned short,3 >, itk::InterpolateImageFunction< itk::Image< unsigned short,3 >, double >'),
  ('CuberilleImageToMeshFilter', 'itk::CuberilleImageToMeshFilter', 'itkCuberilleImageToMeshFilterIF3MF3', True, 'itk::Image< float,3 >, itk::Mesh< float,3 >, itk::InterpolateImageFunction< itk::Image< float,3 >, double >'),
)
snake_case_functions = ('mesh_source', 'image_to_mesh_filter', 'cuberille_image_to_mesh_filter', )
