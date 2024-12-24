```
frontend/
├── public/         # 静态资源 (图像, 字体等)
├── src/
│   ├── app/            # Next.js App Router 目录
│   │   ├── (api)/     # 分组路由 - 内部 API
│   │   │   └── api/    # API 路由
│   │   ├── (dashboard)/ # 分组路由 - 仪表盘
│   │   │   └── dashboard/
│   │   │       └── page.tsx # 仪表盘页面
│   │   ├── (auth)/    # 分组路由 - 认证相关
│   │   │   └── signin/
│   │   │       └── page.tsx # 登录页面
│   │   ├── layout.tsx   # 根布局
│   │   └── page.tsx     # 首页
│   ├── components/     # 可复用 UI 组件
│   │   ├── ui/        # 原子组件 (Button, Input, etc.)
│   │   └── modules/   # 业务组件 (LoginForm, UserCard, etc.)
│   ├── config/         # 配置文件 (环境变量, 主题等)
│   ├── contexts/       # React Context
│   ├── hooks/          # 自定义 Hooks
│   ├── lib/            # 工具函数, 客户端逻辑
│   ├── types/          # TypeScript 类型定义
│   └── utils/          # 工具函数 (日期格式化, 字符串处理等)
├── .env.example        # 环境变量模板
├── .eslintrc.json      # ESLint 配置
├── .prettierrc.json    # Prettier 配置
├── next.config.js      # Next.js 配置
├── package.json        # 项目依赖
├── pnpm-lock.yaml      # 依赖锁定文件
└── tsconfig.json       # TypeScript 配置
```
