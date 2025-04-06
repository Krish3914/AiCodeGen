dockerfile
# Use an official Node.js image as the base
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the package*.json files to the working directory
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the application code to the working directory
COPY . .

# Build the Angular application
RUN npm run build

# Expose the port the application will run on
EXPOSE 80

# Serve the application
CMD ["npm", "run", "start"]