# ServiceHub

ServiceHub is a project aimed at simplifying the interaction between microservices in a distributed architecture. It provides a centralized hub for managing commands and orchestrating requests between different services in your system.

## Benefits

- **Centralized Management:** ServiceHub enables centralized management of commands and request routing, providing a unified point of interaction for microservices.

- **Routing Flexibility:** The service offers flexible routing configuration, allowing easy customization of request paths between services.

- **WebSocket Interaction:** ServiceHub utilizes websockets for data exchange between microservices, ensuring efficient and low-latency interaction.

## How It Works

1. **Service Registration:** Microservices register with the ServiceHub, specifying their unique names.

2. **Routing Configuration:** System administrators configure request routing by specifying source and target services.

3. **Request Dispatching:** Microservices send requests to the ServiceHub, which orchestrates requests according to the defined routing and directs them to the target services.

## Project Status

The project is in the active design stage. The core logic of the application has not been implemented yet, and the current focus is on designing its future functionality.

If you have ideas, suggestions, or would like to contribute to the project, feel free to create issues and submit pull requests. We welcome your participation in shaping the future of ServiceHub!

# ServiceHub

ServiceHub - это проект, направленный на упрощение взаимодействия между микросервисами в распределенной архитектуре. Он предоставляет централизованный хаб для управления командами и оркестрации запросов между различными сервисами в вашей системе.

## Преимущества

- **Централизованное управление:** ServiceHub позволяет централизованно управлять командами и маршрутизацией запросов, предоставляя единый точку взаимодействия для микросервисов.

- **Гибкость маршрутизации:** Сервис предоставляет гибкую конфигурацию маршрутизации, что позволяет легко настраивать направление запросов между сервисами.

- **Взаимодействие через веб-сокеты:** ServiceHub использует веб-сокеты для обмена данными между микросервисами, обеспечивая эффективное и низколатентное взаимодействие.

## Как это работает

1. **Регистрация сервисов:** Микросервисы регистрируются в ServiceHub, указывая свои уникальные имена.

2. **Конфигурация маршрутизации:** Администратор системы настраивает маршрутизацию запросов, указывая исходные и целевые сервисы.

3. **Отправка запросов:** Микросервисы отправляют запросы на ServiceHub, который оркестрирует запросы в соответствии с заданной маршрутизацией и направляет их к целевым сервисам.

## Статус проекта

Проект находится в стадии активного проектирования. Основная логика приложения еще не написана, и в настоящее время ведется проектирование его будущей функциональности.

Если у вас есть идеи, предложения или вы хотели бы внести свой вклад в развитие проекта, не стесняйтесь создавать issue и отправлять pull requests. Мы рады вашему участию в создании ServiceHub!