# 1. Use official Node.js image
FROM node:latest

# 2. Set working directory
WORKDIR /app

# 3. Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# 4. Copy source code
COPY . .

# 5. Copy .env.local (optional — better to use runtime env vars)
# COPY .env.local .env.local

# 6. Enable source maps
ENV NODE_OPTIONS="--enable-source-maps"

# 7. Expose port
EXPOSE 3000

# 8. Start with dd-trace preloaded
CMD npm run dev
