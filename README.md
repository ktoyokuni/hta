# HTA
Custom nodes for ComfyUI
## FTP Upload
Uploads an incoming image to the specified FTP-Server without saving it locally. Upload can be enabled or disabled.
## Show KSampler Noise
**Full Mode**
In Full mode, the custom node directly uses torch.randn to generate noise at the specified full resolution entirely within the node. This process is completely local, without any involvement of latent space downscaling or subsequent upscaling.

**Latent Mode**
Typically, latent space noise is generated at a reduced resolution (usually 1/8 of the full resolution) and then upscaled. However, in this custom node, the latent mode has been modified to bypass the standard 8× upscaling, meaning it also generates noise directly at the full resolution. In essence, both modes yield full-resolution noise, but Full mode creates it directly while latent mode mimics the conventional latent approach without the resolution change.
