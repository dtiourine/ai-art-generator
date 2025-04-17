from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from src.config import MODELS_DIR, PROCESSED_DATA_DIR
from src.config import batch_size, image_size, nc, nz, ngf, ndf, num_epochs, lr, beta1, ngpu
from src.models.discriminator import Discriminator
from src.models.generator import Generator
from src.train.utils import weights_init, load_data
import torchvision.utils as vutils

app = typer.Typer()

import torch
import torch.optim as optim

@app.command()
def train():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    fixed_noise = torch.randn(64, nz, 1, 1, device=device)  # Batch of latent vectors

    real_label = 1.
    fake_label = 0.

    # Todo: Allow function to train
    netG = Generator(ngpu).to(device)
    netG.apply(weights_init)

    netD = Discriminator(ngpu).to(device)
    netD.apply(weights_init)

    dataloader = load_data()

    optimizerD = optim.RMSprop(netD.parameters(), lr=lr)
    optimizerG = optim.RMSprop(netG.parameters(), lr=lr)

    # Training Loop

    # Lists to keep track of progress
    img_list = []
    G_losses = []
    D_losses = []
    iters = 0
    clip_value = 0.01  # For weight clipping
    n_critic = 5  # Number of discriminator updates per generator update

    print("Starting Training Loop...")
    # For each epoch
    for epoch in range(num_epochs):
        # For each batch in the dataloader
        for i, data in enumerate(dataloader, 0):
            ############################
            # (1) Update D network (critic) n_critic times
            ###########################
            for _ in range(n_critic):
                optimizerD.zero_grad()

                # Format batch
                real_images = data[0].to(device)
                batch_size = real_images.size(0)

                # Forward pass real batch through D
                real_validity = netD(real_images).view(-1)

                noise = torch.randn(batch_size, nz, 1, 1, device=device)
                fake_images = netG(noise)
                fake_validity = netD(fake_images.detach()).view(-1)

                errD = -torch.mean(real_validity) + torch.mean(fake_validity)

                errD.backward()
                optimizerD.step()

                for p in netD.parameters():
                    p.data.clamp_(-clip_value, clip_value)

            # Track statistics for logging
            D_x = real_validity.mean().item()  # Average critic score on real data
            D_G_z1 = fake_validity.mean().item()  # Average critic score on fake data

            ############################
            # (2) Update G network once per n_critic iterations
            ###########################

            optimizerG.zero_grad()
            noise = torch.randn(batch_size, nz, 1, 1, device=device)
            fake_images = netG(noise)
            fake_validity = netD(fake_images)
            errG = -torch.mean(fake_validity)
            errG.backward()
            optimizerG.step()

            # Track more statistics
            D_G_z2 = fake_validity.mean().item()  # New average critic score on fake data after G update

            # Output training stats
            if i % 50 == 0:
                print('[%d/%d][%d/%d]\tLoss_D: %.4f\tLoss_G: %.4f\tD(x): %.4f\tD(G(z)): %.4f / %.4f'
                      % (epoch, num_epochs, i, len(dataloader),
                         errD.item(), errG.item(), D_x, D_G_z1, D_G_z2))

            # Save Losses for plotting later
            G_losses.append(errG.item())
            D_losses.append(errD.item())

            # Check how the generator is doing by saving G's output on fixed_noise
            if (iters % 500 == 0) or ((epoch == num_epochs - 1) and (i == len(dataloader) - 1)):
                with torch.no_grad():
                    fake = netG(fixed_noise).detach().cpu()
                img_list.append(vutils.make_grid(fake, padding=2, normalize=True))

            iters += 1


if __name__ == "__main__":
    app()
