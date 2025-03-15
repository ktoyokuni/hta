# HTA
Custom nodes for ComfyUI
## FTP Upload
Uploads an incoming image to the specified FTP-Server without saving it locally. Upload can be enabled or disabled.
## Native Noise
Generates reproducible random noise patterns at specified dimensions according to the method used by the KSampler. It creates channel-separated Gaussian noise (torch.randn) with consistent seed-based randomization across R, G, and B channels, then normalizes values to [0-1] range. Each color channel uses a different deterministic seed offset to ensure varied yet reproducible patterns.
