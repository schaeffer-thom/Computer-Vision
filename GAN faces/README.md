# GAN Faces with PyTorch

This project implements a **Generative Adversarial Network (GAN)** from scratch in PyTorch to generate human-like face images. It serves as a minimal, educational introduction to GAN architecture and training procedures using a subset of real-world facial data.

> Developed by Thomas Schaeffer  
> Date: Fall 2023  

---

## Project Goals

- Build a simple GAN architecture (Generator + Discriminator)
- Train on real face images to synthesize realistic outputs
- Visualize training progress through generated samples
- Understand core GAN principles: adversarial loss, generator/discriminator balance, mode collapse

---

## Tech Stack

- **Language**: Python  
- **Framework**: PyTorch  
- **Visualization**: Matplotlib  
- **Data**: Aligned and cropped face images (e.g., CelebA subset or similar)

---

## Model Architecture

### Generator
Takes a latent noise vector and outputs a fake image:

```python
nn.Sequential(
    nn.Linear(latent_dim, 128),
    nn.ReLU(),
    nn.Linear(128, 256),
    nn.ReLU(),
    nn.Linear(256, image_size),
    nn.Tanh()
)
