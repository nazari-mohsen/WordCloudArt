# WordCloudArt: Generating Beautiful Word Clouds with Customization

This project is the **backend** for an Android application that uses **Django REST Framework** along with the [**word_cloud**](https://github.com/amueller/word_cloud) package to generate customizable word clouds. Key features include support for the Persian language, caching with **Redis**, task queue management with **Celery**, and data storage in **MariaDB**.

![Sample app image](https://github.com/nazari-mohsen/WordCloudArt/blob/main/images/0ZNEy5t8yFP902854.jpeg)

## Features

- Persian language support for generating word clouds.
- Option to use a custom image as a mask for the word cloud.
- Customizable font, size, and word count for word clouds.
- Background and font color customization.
- In-app coin purchases and rewards from watching ads.
- Advanced word filters to block inappropriate terms.
- No registration required: Users are identified by a unique code generated upon first installation.
- Unique code generation: The app generates a unique identifier (ID) for each user based on device-specific data such as **IMEI**, **Android ID**, and other relevant details.
- Persistent unique ID: Even if the app is uninstalled and reinstalled, the same unique code is assigned to the user to ensure continuity and avoid data loss.
- The unique ID is generated and saved locally, allowing it to persist across app re-installs.
- The app checks the version on first launch and suggests updating to the latest version if an older version is detected.
- Use of **JWT** for secure authentication and session management.
- Use of **Swagger** for automatic API documentation and providing a user-friendly interface for testing requests.
- Caching with **Redis** to optimize performance.
- **Celery** to handle long-running tasks.
- **Flower** for monitoring and managing Celery tasks
- **MariaDB** for storing data.
- Persian-language admin panel for easier management.
- Watermark feature to add custom text on generated word clouds.

## Prerequisites

Ensure you have the following software installed:

- Python 3.6
- Docker and Docker Compose
- Redis
- Celery
- MariaDB

## Installation and Setup with Docker Compose

Follow these steps to run the backend using Docker Compose:

1. **Clone the project**:
    ```bash
    git clone https://github.com/nazari-mohsen/WordCloudArt.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd WordCloudArt
    ```

3. The project includes a pre-configured `docker-compose.yml` file to set up all required services.

4. **Build and start the containers**:
    ```bash
    docker-compose up --build
    ```

    This will start all the necessary services: Django, Redis, MariaDB, and Celery.

5. Once the containers are running, the **API Docs** will be available at [http://localhost:8000/api/v1/docs/](http://localhost:8000/api/v1/docs/).

6. To access the Flower panel, visit: [http://localhost:5555](http://localhost:5555)

## Persian Admin Panel

This backend includes a **Persian-language admin panel** for managing data and settings.

Access the **Admin Panel** at: [http://localhost:8000/admin/](http://localhost:8000/admin/).

### Admin Panel - Dashboard

The dashboard provides essential information such as user count, coins, and app performance.

![Sample Output 1](https://github.com/nazari-mohsen/WordCloudArt/blob/main/images/21-46-37.png)

![Sample Output 2](https://github.com/nazari-mohsen/WordCloudArt/blob/main/images/21-47-45.png)

### Features in the Admin Panel

- **User Management**: View and manage user information.
- **Coin Management**: Update users' coin balances.
- **Word Filter Management**: Manage inappropriate words.
- **Ad Management**: Configure ads to allow users to earn coins.

## Challenges and Solutions

- **Persian Language Support**: Initially, the `word_cloud` package didn't support Persian. I added custom code to enable full Persian support.
- **Inappropriate Word Filtering**: A system was developed to detect and block inappropriate words.
- **Caching Coins**: For caching coins, it was necessary to use Redis in a structured way to ensure that the data remains up-to-date while also being cached, ensuring optimal system performance.
## Sample Outputs

Here are some examples of word clouds generated by the app.

### Sample Output 1

![Sample 1](https://github.com/nazari-mohsen/WordCloudArt/blob/main/images/42NDIH8K6ClI111199.jpeg)

### Sample Output 2

![Sample 2](https://github.com/nazari-mohsen/WordCloudArt/blob/main/images/3593yFDewd7N114415.jpeg)

### Sample Output 3

![Sample 3](https://github.com/nazari-mohsen/WordCloudArt/blob/main/images/52vNVXGw5wqv222854.jpeg)


## Contributing

To contribute:

1. Fork the project.
2. Create a new branch.
3. Make your changes.
4. Submit a Pull Request.

## Reporting Issues

For any issues or questions, please visit the [Issues](https://github.com/nazari-mohsen/WordCloudArt/issues) page.

## License

This project is licensed under the Apache License. See the LICENSE file for more details.
