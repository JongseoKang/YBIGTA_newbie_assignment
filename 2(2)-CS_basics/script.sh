#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" &>/dev/null
}

# Path to Anaconda installer
ANACONDA_INSTALLER="Anaconda3-2024.10-1-Linux-x86_64.sh"
INSTALL_URL="https://repo.anaconda.com/archive/$ANACONDA_INSTALLER"

# Check if conda is installed
if command_exists conda; then
    echo "Anaconda is already installed."
else
    echo "Anaconda is not installed. Proceeding with installation..."

    # Download the Anaconda installer
    if [ ! -f "$ANACONDA_INSTALLER" ]; then
        echo "Downloading Anaconda installer..."
        wget $INSTALL_URL -O $ANACONDA_INSTALLER
    fi

    # Install Anaconda
    echo "Installing Anaconda..."
    bash "$ANACONDA_INSTALLER" -b -p $HOME/anaconda3

    # Add Anaconda to PATH
    echo "Adding Anaconda to PATH..."
    export PATH="$HOME/anaconda3/bin:$PATH"
    echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >>~/.bashrc

    # Reload bash configuration
    source ~/.bashrc
    conda --version
fi

# Activate the specified environment
conda init 

ENV_NAME="myenv"
if conda env list | grep -q "^$ENV_NAME "; then
    echo "Activating Anaconda environment '$ENV_NAME'..."
    conda activate $ENV_NAME
else
    echo "Environment '$ENV_NAME' not found. Creating it..."
    conda create -n $ENV_NAME python=3.9 -y
    conda init
    conda activate $ENV_NAME
fi

list=("2243" "3080" "3653" "5670" "10830" "17408")
for var in $list
do 
    input="./input/input_'$var'"
    output="./output/output_'$var'"

    if [[ -f "$script" ]]; then
        echo "Running script: $script with input: $input"

        # Run the Python script with the input and compare the output
        python3 "$script" < "$input" > "$output"
    else
        echo "Script $script does not exist. Skipping."
    fi
done