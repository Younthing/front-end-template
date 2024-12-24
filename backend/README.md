```
my_fastapi_project/
├── src/
│   └── app/
│       ├── __init__.py
│       ├── main.py              # FastAPI 应用程序入口点
│       ├── core/               # 核心配置
│       │   ├── __init__.py
│       │   ├── config.py       # 配置设置
│       │   └── settings.py     # 环境变量和设置
│       │
│       ├── api/                # API 路由
│       │   ├── __init__.py
│       │   ├── v1/            # API 版本 1
│       │   │   ├── __init__.py
│       │   │   └── endpoints/  # API 端点
│       │   │       ├── __init__.py
│       │   │       ├── users.py
│       │   │       └── items.py
│       │   └── dependencies.py # 共享依赖
│       │
│       ├── models/            # 数据库模型
│       │   ├── __init__.py
│       │   └── user.py
│       │
│       ├── schemas/           # Pydantic 模型/模式
│       │   ├── __init__.py
│       │   └── user.py
│       │
│       ├── crud/             # CRUD 操作
│       │   ├── __init__.py
│       │   └── user.py
│       │
│       ├── db/               # 数据库配置
│       │   ├── __init__.py
│       │   └── session.py
│       │
│       ├── services/         # 业务逻辑服务
│       │   ├── __init__.py
│       │   └── user_service.py
│       │
│       └── utils/            # 工具函数
│           ├── __init__.py
│           └── common.py
│
├── tests/                    # 测试文件
│   ├── __init__.py
│   ├── conftest.py          # pytest 配置
│   ├── test_api/
│   └── test_services/
│
├── alembic/                  # 数据库迁移
│   ├── versions/
│   ├── env.py
│   └── alembic.ini
│
├── pyproject.toml           # Poetry 项目配置
├── .env                     # 环境变量
├── .env.example            # 环境变量示例
├── .gitignore
└── README.md
```
