# Learning Goals:

1. Windowing with OpenGL with platform-independant GLFW API
   1. Windowing
   2. Reading & Processing Inputs
   3. Handling Events
   4. Background Images, Textures, Surfaces, ...

2. Create some Pixels/Voxels

3. Create Editor to place Voxels/Blocks/Spirtes,...

4. Applied LA for "roaming/creative mode" camera

5. Play around with "falling sand"-like simulations / celluar automata

# Environment:
1. All runtime requirements should be reflected in pyproject.to
   1. All transitive stuff must be installable via pip
      1. This ensures that tox will run fine => easy move to CI &  
      2. glfw is fine, because the .dll bits are contained within the wheel
      3. PyOpenGL_accelerate is NOT fine, because it requires Microsoft Visual C++ (MSVC) on the machine
      
