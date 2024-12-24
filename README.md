# 前后端分离项目模板

这个项目模板提供了一个基于 Next.js 的前端和 Python (Poetry) 的后端基础架构。

## 项目结构

```
.
├── frontend/    # Next.js 前端项目
└── backend/     # Python 后端项目
```

## 初始化步骤

### 前端设置 (Next.js)

```bash
# 使用 pnpm 创建 Next.js 项目
npx create-next-app@latest frontend --use-pnpm

# 进入前端目录
cd frontend

# 安装依赖
pnpm install
```

### 后端设置 (Python + Poetry)

```bash
# 创建 Python 项目
poetry new backend

# 进入后端目录
cd backend

# 初始化虚拟环境
poetry install
```

## 开发指南

### 前端开发

```bash
cd frontend
pnpm dev        # 启动开发服务器
pnpm build      # 构建生产版本
pnpm start      # 运行生产版本
```

### 后端开发

```bash
cd backend
poetry shell    # 激活虚拟环境
poetry run python main.py  # 运行后端服务
```

## 技术栈

### 前端

- Next.js
- React
- TypeScript
- Tailwind CSS

### 后端

- Python
- Poetry
- FastAPI

## 注意事项

- 确保已安装 Node.js 和 pnpm
- 确保已安装 Python 3.12+ 和 Poetry
- 开发时请遵循各自的编码规范
