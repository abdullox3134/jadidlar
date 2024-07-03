# What is Docker?
## What is docker container
A Docker container is a lightweight, standalone, and executable package that includes everything needed to run a piece of software, including the code, runtime, system tools, libraries, and settings. Containers leverage the host operating system's kernel but run isolated processes, ensuring consistency across different environments. This makes Docker containers highly portable, efficient, and reproducible, ideal for application development, testing, and deployment. By using containers, developers can ensure their applications run smoothly in any environment, from local machines to cloud servers.
## What is Dockerhub
DockerHub is a cloud-based registry service that allows you to link code repositories, build images, and test them. It simplifies container management and distribution, making it easy to deploy Docker containers.
## Using Docker containers to run applications on a server offers several advantages over running applications without isolation or containers

1. **Portability**: Containers encapsulate the application and its dependencies, ensuring it runs consistently across different environments, from development to production.

2. **Isolation**: Each container runs in its own isolated environment, preventing conflicts between applications and their dependencies. This improves security and stability.

3. **Resource Efficiency**: Containers share the host OS kernel, making them more lightweight and efficient compared to virtual machines. This allows for higher density and better resource utilization on servers.

4. **Scalability**: Containers can be easily scaled up or down to handle varying workloads. Orchestration tools like Kubernetes can automate scaling and load balancing.

5. **Fast Deployment**: Containers can be started and stopped quickly, enabling rapid deployment and updates. This accelerates the development and release cycles.

6. **Consistency**: By packaging the application and its environment together, containers eliminate the "it works on my machine" problem, ensuring consistent behavior across different stages of the development pipeline.

7. **Simplified Management**: Tools like Docker Compose and Docker Swarm simplify the management of multi-container applications, making it easier to define and run complex applications.

8. **Improved Security**: Containers provide an additional layer of security by isolating applications, which can help mitigate the impact of potential vulnerabilities and breaches.

By using Docker containers, you can achieve greater efficiency, consistency, and control over your application deployments, leading to more reliable and maintainable server environments.


# How to build, update and deploy application to Dockerhub

1. Login DockerHub account!
   
      ```
      sudo docker login
      ```
      
    - DockerHub username: `userhubdocker1`
    - DockerHub Password: `Docker_hub`
    - DockerHub Gmail: `rldockerhub@gmail.com`
    - OUTPUT: `Login Succeeded`
2. Build docker __Image__
    - Change directory to located code and Dockerfile
    - Build docker __Image__ in your localhost
      ```
      docker build -t userhubdocker1/jadid-backend:1 .
      ```
    - Every time change tag of image
3. Push Image to __DockerHub__
     - You need to deploy your Image to DockerHub for use anytime and anywhere without access!

      ```
       sudo docker push userhubdocker1/jadid-backend:1
      ```

4. Deploy container to server
     - First Check in localhost for container working correctly
     - Stop running contanier on server for update

       ```
         docker stop container_id
       ```
       
      -  Run contanier with new version tag

       
       docker run -d -p 8009:8000 -v /var/www/raqamlilab/jadidlar/jadidlar/media:/app/media userhubdocker1/jadid-backend:1

5. Make sure to container working!
   - If container stop or failed suddenly: Stop container and change container version with previus tag 
 
