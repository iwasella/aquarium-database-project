# aquarium-database-project

To get started:
Install nvm (node version manager) for your OS, nvm-windows for Windows or nvm for macOS/Ubuntu.

Verify it's installed correctly with the following command (you may need to restart your terminal):
- `nvm --version`

Install latest long-term supported (LTS) version of node with:
- `nvm install lts`

Set current node version to the LTS version with
- `nvm use <version>`

Verify node/npm were correctly installed with:
- `node -v`
- `npm -v`

Install dependencies with:
- `npm install`

You should see a node_modules folder be created. Add this folder to your .gitignore file.

Test to see if you can run the app with
- `npm start`

You should see something like:
```
> aquarium-database-project@0.0.0 start
> node ./bin/www

  aquarium-database-project:server Listening on port 3000 +0ms
```

Verify the server is working by navigating to http://localhost:3000/ in your preferred browser. You should be redirected to the app page at /store/menu.

The following scripts are also available to start the server:
`npm run devstart` and `npm run unix-serverstart` / `npm run windows-serverstart`
- The devstart script enables automatically restarting the server when you make changes to files. 
- The serverstart scripts specify the DEBUG variable to enable console logging/debugging and then calls `npm run devstart`. 

You can look at the scripts section in the package.json to see the precise commands.