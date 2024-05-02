# Neural Radiance Fields (NeRF)

## Volumetric Rendering
Represent a 3D scene as a function $F(x, y, z, \theta, \phi) \to (RGB, \sigma)$.
$\sigma$ = Density (Alpha).

## Ray Marching
Shoot rays from camera through pixels. 
Accumulate color and density along the ray.
Differentiable rendering allows training from 2D photos.

## Gaussian Splatting
Newer technique. Represent scene as cloud of 3D Gaussians. Faster rendering (Real-time).
