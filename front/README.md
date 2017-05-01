## Install
``` bash
# Clone the repository
$ git clone https://github.com/kr1an/star-seeker

# Go into the repository
$ cd star-seeker

# Install dependencies
$ npm install
```

## Usage
Run this two commands in two different prompts to start developing with hot reloading.
``` bash
# Webpack builds once and watches for changes to apply
$ npm run dev

# Start electron app
$ npm start
```

## What's included
- JSX support for React using Babel.
- ES6 native support for React via Node (this is Electron, no need for Babel to transpile ES6).
- CSS modules support.
- JS, CSS and assets bundling with hot reloading via Webpack 2.


## Folder structure
```
├── electron-react-webpack/             # Your project's name

    ├── app/

        ├── build/                      # Webpack 2 will create and update this folder
            ├── bundle.css              # Bundled CSS
            ├── bundle.js               # Bundled JS
            ├── ...                     # Your images will be copied here

        ├── src/

            ├── assets/                 # Images
                ├── electron.png
                ├── react.png
                ├── webpack.png

            ├── components/             # React Components
                ├── Link.jsx
                ├── Logo.jsx

            ├── styles/                 
                ├── Local.css           # Local CSS
                ├── Global.css          # Global CSS and constants

            ├── App.jsx                 # React main component
            ├── entry.js                # App entry. Your global JS can go here

        ├── index.html                  # Single Page Application HTML, it only uses build's files

    ├── main.js                         # Electron app
    ├── package.json
    ├── webpack.config.js               # Webpack 2 setup
```
