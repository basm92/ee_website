## ee_website

Repository for the Empirical Economics course (UU 2025-2026). The website is built using Quarto and accessible [here](http://basm92.quarto.pub/empirical-economics). 


### How to install the necessary Python environment

Prerequisite: you need to download and install the `uv` Python package manager: https://docs.astral.sh/uv/getting-started/installation/. 

- Step 1: Get the Project Files

```
git clone <your-repository-url>
cd <your-project-folder>
```

- Step 2: Step 2: Sync the Environment with uv sync

```
uv sync
```

- Step 3: Activate the uv environment (Linux/MacOS), in the project folder:

```
source .venv/bin/activate
```

On Windows:

``` 
.venv\Scripts\activate
```

And that's it! The new computer now has an identical, fully functional development environment, ready for work. 

### How to compile the slides

- Step 4: Install Quarto (On Linux/MacOS)

```
sudo apt install quarto
```

- Step 5: Render the slides

```
quarto preview ~/lectures/lecture1/lecture1.qmd --no-browser --no-watch-inputs
```

### Credits

Thanks to Mads Nielsen, Jelena Arsenijevic, Tina Dulam, Vincent Kunst, Stanislav Avdeev and Soenke Matthewes for offering many corrections, improvements, suggestions and ideas.
