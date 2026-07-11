<div align="center">

# PG.skill

> _"Writing doesn't just communicate ideas; it generates them."_

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue)](https://github.com/FranklinNexus/paul-graham-skills)
[![Runtime](https://img.shields.io/badge/Runtime-Codex%20%7C%20Cursor%20%7C%20Claude%20%7C%20Antigravity-lightgrey)](https://github.com/FranklinNexus/paul-graham-skills)
[![Distilled](https://img.shields.io/badge/Type-Behavioral%20Framework-orange)](PRINCIPLES.md)

<p align="center">
  <img src="assets/paul-graham.jpg" alt="Paul Graham" width="360" />
</p>

<br>

**Paul Graham 的创业与写作操作系统。不是语录复读，是可运行的判断框架。**

<br>

从 PG 式创业判断、用户痴迷、独立思考、Maker 时间与清晰写作中提炼而成，  
封装为 `SKILL.md` + `PLAYBOOK.md`：能路由问题、识别瓶颈、给出可验证的下一步。

[看效果](#效果示例) · [安装](#安装) · [蒸馏了什么](#蒸馏了什么) · [FAQ](#faq)

</div>

---

## 效果示例

### 问：我有个创业想法，听起来很蠢，但身边有几个人特别上头。这值得做吗？

```
PG 式判断 ❯  先别问「蠢不蠢」，先问「谁上头，上头到什么程度」。

              大多数人的问题是：还没有几个用户真的离不开你，
              就开始担心 idea 听起来不够体面。

              你要找的不是礼貌点头，而是：
              有人愿意忍受粗糙的产品、反复试用、主动推荐给朋友。

              如果只有「听起来不错」，那是弱信号。
              如果有人愿意为你的 v0 改计划、催你发版、
              甚至因为用不了而生气——这才是值得继续的信号。

              下一步：列出 3 个「上头用户」各自愿意做的具体行为，
              以及你本周能交付的最小可玩版本。
```

### 问：我日历全是会，根本没时间写代码。怎么办？

```
PG 式判断 ❯  你不是没时间，是被 Manager Schedule 吃掉了。

              Maker 的工作需要连续大块时间。
              一个会议切开的下午，对写代码的人来说不是「少了一小时」，
              而是「今天没了」。

              先把下周砍到：每天至少一个 3 小时、无会议、
              只做最重要制作任务的块。
              其他会能推则推，能异步则异步。

              如果砍不掉，说明你现在的工作形态已经不是 Maker 了——
              要么换角色，要么接受产出会长期偏低。
```

### 问：我写的文章很顺，但读者说「看完了也不知道你想说什么」。

```
PG 式判断 ❯  顺，不等于清楚。

              很多文章是在用漂亮的句子绕开真正的想法。
              写作不是把已经想好的东西记录下来——
              写作本身就是思考过程。

              先写一句：这篇文章到底发现了什么？
              如果这句话写不出来，文章还没开始。

              然后删掉所有只为显得聪明的开场、
              所有没有观察支撑的空话，
              保留一句让你自己意外的那句话，围绕它重写。
```

> 这不是让 AI 扮演 PG。它调用的是同一套**问题路由 + 证据检验 + 瓶颈识别**方法，把回答压到可执行的下一步。

---

## 安装

### Codex（推荐）

让 Codex 直接从 GitHub 安装本仓库中的 skill，或在克隆后运行：

```powershell
.\scripts\install.ps1 -Platform codex
```

安装目标为 `~/.codex/skills/`。重启 Codex 后生效。

### 其他 Agent Runtime

本仓库是独立的 Agent Skill 包，支持 **Cursor · Claude Code · Antigravity（AGENTS.md）**。

### 方式一：一键安装脚本（推荐）

```powershell
git clone https://github.com/FranklinNexus/paul-graham-skills.git
cd paul-graham-skills
.\scripts\install.ps1 -Platform cursor
```

安装到 Claude Code：

```powershell
.\scripts\install.ps1 -Platform claude
```

安装到项目内 Antigravity / AGENTS.md：

```powershell
.\scripts\install.ps1 -Platform antigravity -Scope project -ProjectPath "C:\path\to\project"
```

全部平台：

```powershell
.\scripts\install.ps1 -Platform all
```

### 方式二：手动安装

| Runtime | 路径 |
| --- | --- |
| Cursor | `~/.cursor/skills/paul-graham/` |
| Claude Code | `~/.claude/skills/paul-graham/` |
| Antigravity | 项目内 `.agents/skills/paul-graham.md` + `AGENTS.md` 引用 |

复制 `skills/paul-graham/` 整个目录，或按 `adapters/` 里的说明接入。

### 使用

安装后，在对话里直接说：

```
> 用 PG 的视角帮我判断这个创业想法
> Paul Graham 会怎么看我这个产品方向？
> 帮我用 PG 的方式改这篇 essay 的结构
> 我会议太多，用 maker schedule 的思路帮我排一周
```

显式触发词：`PG` · `Paul Graham` · `YC` · `创业想法` · `用户爱` · `写作` · `maker time`

---

## 蒸馏了什么

### 6 个核心原则

| 原则 | 一句话 | 解决什么 |
| --- | --- | --- |
| **从异常出发** | 好想法来自真实用户痛点，不是市场地图 | 追风口、无用户 |
| **少而狂热** | 几个真正热爱的用户 > 一群礼貌点赞 | 把点赞当 PMF |
| **写作即思考** | 写不清楚 = 还没想清楚 | 文章顺但空洞 |
| **保护 Maker 时间** | 连续大块时间比碎片「高效」更重要 | 会多、产出少 |
| **怪异可能是信号** | 聪明人先否定的想法，值得先验证 | 过早自我审查 |
| **选对方向再用力** | 努力只在正确方向上复利 | 勤奋但原地打转 |

### 5 类问题路由

`PLAYBOOK.md` 会把请求分到：

1. **创业想法** — 怪异早期 idea 是否值得测
2. **创始人问题** — 决心、灵活性、用户接触
3. **写作问题** — essay、memo、pitch 结构
4. **职业/项目选择** — 该做什么
5. **时间/专注** — 会议、状态工作、深度制作

### 输出形态

典型回答结构：

```markdown
### PG-Style Diagnosis
[直接判断]

### Real Bottleneck
[当前真正卡住的地方]

### Evidence Gap
- [还缺什么证据]

### Next 7 Days
- [可验证动作]
```

### 内置防线

- **Failure Modes**：防止从市场报告出发、把礼貌当需求、用写作藏住模糊思考
- **Edge Cases**：怪创始人、好 pitch 坏产品、该融资还是该做用户
- **Self-Test**：回答前自检是否给了具体下一步

详见 [`PRINCIPLES.md`](PRINCIPLES.md) · [`EVALUATION.md`](EVALUATION.md) · [`skills/paul-graham/PLAYBOOK.md`](skills/paul-graham/PLAYBOOK.md)

---

## 仓库结构

```text
paul-graham-skills/
├── README.md                 # 你正在看的说明
├── PRINCIPLES.md             # 人类可读原则摘要
├── EVALUATION.md             # 自测 prompt
├── PUBLISH.md                # 发布检查清单
├── skills/paul-graham/
│   ├── SKILL.md              # Agent 入口（自动加载）
│   └── PLAYBOOK.md           # 复杂场景 playbook
├── .agents/skills/paul-graham.md
├── adapters/                 # AGENTS.md / GEMINI 模板
└── scripts/
    ├── install.ps1
    └── validate.py
```

---

## 参考语料

本仓库是 **PG 公开文章的行为蒸馏**（`SKILL.md` / `PLAYBOOK.md`），不是全文库。  
若需阅读 **Paul Graham 中文译文**，见 [PG · Sam · 张一鸣中文译文库 → `paul-graham/`](https://github.com/FranklinNexus/pg-sam-zym-blog-zh/tree/main/paul-graham)。
材料均为**互联网上的公开记录**；说明见 [NOTICE.md](https://github.com/FranklinNexus/pg-sam-zym-blog-zh/blob/main/NOTICE.md)。

---

## 边界说明

- 这是**蒸馏后的行为框架**，不是 PG 文章镜像，不包含长文引用或原文重建。
- **不扮演 Paul Graham**，不声称「PG 本人会说」。
- 用于分析、写作结构、创业判断；**不构成投资或法律建议**。

完整政策见 [`SOURCE_POLICY.md`](SOURCE_POLICY.md)。

---

<div align="center">

**装上去，不是为了多一个名人滤镜，而是多一套能帮你发现异常、保护制作时间、把思考写清楚的判断系统。**

</div>
