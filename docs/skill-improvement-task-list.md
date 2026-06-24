# Ed-PhD-Copilot-Skills 逐步完善任务清单

> 生成日期：2026-06-23  
> 适用项目：`Ed-PhD-Copilot-Skills`
> 参照基准：`Supervisor-Skills` 的完整度、分层结构、参考材料体系、评分规则、示例输出、反例库和可执行检查机制。  
> 三个优先级：补齐 `references/` 支撑体系、强化核心技能、建立贯穿式真实样例。  
> 当前基线：项目已进入 V1.0 安装前可用状态；本清单用于下一轮持续完善、验证和学术化加固。

## 一、总体目标

将 `Ed-PhD-Copilot-Skills` 从“可安装、可使用的教育信息化治理方向技能库”进一步提升为“可长期迭代、可复核、可迁移到真实博士研究任务中的专业技能体系”。

具体目标包括：

- 让每个技能都有明确的触发边界、输入要求、执行步骤、引用材料和输出格式。
- 让每个评价、判断、审查和建议都有可复核的评分锚点或证据依据。
- 让技能输出能够稳定服务教育技术、教育领导与管理、教育信息化治理方向的博士研究任务。
- 让贯穿案例、失败案例和真实课题案例共同形成回归测试体系。
- 让项目在协议、署名、文献依据、安装结构和质量检查上保持可发布状态。

## 二、当前基线盘点

### 2.1 已具备的项目基础

- **目标**：明确当前仓库已经完成的基础，避免重复建设。
- **当前状态**：
  - 已建立 7 个技能：选题评估、引言起草、论文模板、混合研究证据、图示设计、投稿前审查、AI 辅助研究流程。
  - 每个技能均已有 `SKILL.md`、`agents/openai.yaml` 和 `references/`。
  - 已建立贯穿案例：`docs/case-multi-agent-smart-campus.md`。
  - 已生成 7 个正向样例输出：`docs/examples/01-...` 至 `07-...`。
  - 已建立失败案例目录：`docs/examples/failure-cases/`。
  - 已建立结构检查脚本：`scripts/check_skill_structure.py`。
  - 已建立来源与证据文件：`docs/evidence-base.md`、`docs/verified-source-registry.md`、`docs/chinese-core-literature-inventory.md`。
  - 已采用与 `Supervisor-Skills` 兼容的 `CC BY-NC-SA 4.0` 协议，并在 `NOTICE.md` 中署名。
- **实施路径**：
  - 每次迭代前先运行结构检查脚本。
  - 每次新增 reference、example 或规则后同步更新覆盖矩阵。
  - 每次发布前检查 README、CHANGELOG、审计文件和许可证说明。
- **产物路径**：
  - `scripts/check_skill_structure.py`
  - `docs/skill-coverage-matrix.md`
  - `docs/install-readiness-audit.md`
  - `CHANGELOG.md`
- **验收标准**：
  - 仓库结构检查通过。
  - README 中的成熟度说明与实际文件一致。
  - 未核验文献不被写成正式引用。

### 2.2 仍需持续完善的问题

- **目标**：把后续工作聚焦在质量提升，而不是简单堆文件。
- **待完善点**：
  - 中文核心/CSSCI 文献仍需进一步核验和题录化。
  - 当前贯穿案例偏“智能校园治理”，需要更多教育技术真实场景。
  - 失败案例还可以进一步变成可自动检查的回归测试。
  - 核心技能之间的路由关系还可以更强，例如从选题评估自动进入论文模板和证据设计。
  - 方法学 reference 需要继续补强准实验、案例研究、政策文本分析、学习分析、设计科学研究等细分路径。
  - `agents/openai.yaml` 与 `SKILL.md` 的触发描述需要随内容更新定期校准。
- **实施路径**：
  - 将后续工作分为 P1、P2、P3 三个优先级批次。
  - 每个批次都采用“补材料 -> 改技能 -> 跑案例 -> 修输出 -> 记录审计”的闭环。
- **验收标准**：
  - 每个批次都有明确产物。
  - 每个批次结束后都能生成一份评审或审计记录。

## 三、优先级一：补齐 references 支撑体系

### 3.1 建立 references 总目录与使用说明

- **目标**：让使用者和后续维护者知道每个 reference 的作用、读取时机和适用任务。
- **实施路径**：
  - 在 `plugins/ed-phd-copilot/skills/README.md` 中增加 references 导航表。
  - 为 7 个技能分别列出“必读 reference”和“按任务读取 reference”。
  - 标注每个 reference 属于评分规则、方法模板、写作模板、伦理规则、失败案例还是示例输出。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/README.md`
  - `docs/skill-coverage-matrix.md`
- **验收标准**：
  - 用户不打开具体技能文件，也能知道每个技能有哪些支撑材料。
  - 每个 reference 都能说清“何时读取、解决什么问题”。

### 3.2 完善 `governance-idea-evaluator` 参考体系

- **目标**：将选题评估技能打造成所有研究任务的入口闸门。
- **实施路径**：
  - 检查 `references/rubric.md` 是否覆盖政策相关性、教育价值、组织可行性、人智协同、方法可证性、伦理可控性、理论贡献。
  - 检查 `references/fatal-flaws.md` 是否包含 CRITICAL 级短路规则。
  - 扩展 `references/theory-anchors.md`，补充教育领导力、组织学习、制度理论、技术采纳、数据治理、算法治理等理论锚点。
  - 在 `references/worked-examples.md` 中增加至少 3 个不同质量层级的选题：高潜力选题、需重构选题、应放弃或转向选题。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/governance-idea-evaluator/references/rubric.md`
  - `plugins/ed-phd-copilot/skills/governance-idea-evaluator/references/fatal-flaws.md`
  - `plugins/ed-phd-copilot/skills/governance-idea-evaluator/references/theory-anchors.md`
  - `plugins/ed-phd-copilot/skills/governance-idea-evaluator/references/worked-examples.md`
- **验收标准**：
  - 输入一个博士选题后，技能能输出评分、短板、红线风险、修改路径和下一步路由。
  - 出现伦理不可控、证据错配、理论真空、技术先行无治理问题时，能明确建议 `Pivot`。

### 3.3 完善 `edtech-intro-drafter` 参考体系

- **目标**：让引言起草不只是列段落，而能形成教育技术论文的论证链。
- **实施路径**：
  - 补强 `references/four-part-logic.md`，明确政策背景、技术变革、治理困境、研究合法性之间的递进关系。
  - 扩展 `references/paragraph-patterns.md`，为六段式引言提供段落功能、可用句型、证据要求和错误示例。
  - 扩展 `references/alienation-patterns.md`，补充数字形式主义、平台依赖、数据孤岛、算法不透明、教师负担转移、学生数据权益风险等问题模式。
  - 增加不同论文类型的引言样例：政策分析类、机制构建类、实证研究类、设计科学类。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/edtech-intro-drafter/references/four-part-logic.md`
  - `plugins/ed-phd-copilot/skills/edtech-intro-drafter/references/paragraph-patterns.md`
  - `plugins/ed-phd-copilot/skills/edtech-intro-drafter/references/alienation-patterns.md`
  - `plugins/ed-phd-copilot/skills/edtech-intro-drafter/references/worked-examples.md`
- **验收标准**：
  - 每段引言都能说明其学术功能、核心论点和证据需求。
  - 输出能够直接扩写为 CSSCI 或博士论文开题报告中的研究背景部分。

### 3.4 完善 `governance-paper-template` 参考体系

- **目标**：让论文模板能够支撑机制构建、系统架构、指标体系、设计科学和治理实践类论文。
- **实施路径**：
  - 扩展 `references/paper-types.md`，明确不同论文类型的适用条件、典型结构和风险。
  - 扩展 `references/theory-to-design.md`，建立“理论概念 -> 治理问题 -> 设计原则 -> 系统模块 -> 证据指标”的映射。
  - 补强 `references/dual-topology.md`，把技术架构与治理架构并列呈现。
  - 细化 `references/section-skeleton.md`，提供博士论文、期刊论文、开题报告三种结构版本。
  - 增加“贡献声明”模板，区分理论贡献、方法贡献、实践贡献和政策启示。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/governance-paper-template/references/paper-types.md`
  - `plugins/ed-phd-copilot/skills/governance-paper-template/references/theory-to-design.md`
  - `plugins/ed-phd-copilot/skills/governance-paper-template/references/dual-topology.md`
  - `plugins/ed-phd-copilot/skills/governance-paper-template/references/section-skeleton.md`
  - `plugins/ed-phd-copilot/skills/governance-paper-template/references/worked-examples.md`
- **验收标准**：
  - 用户给出一个研究设想后，技能能输出论文类型判断、章节结构、理论-机制-系统-证据矩阵。
  - 每个章节都有功能说明、关键论点、所需证据和常见风险。

### 3.5 完善 `mixed-methods-evidence-template` 参考体系

- **目标**：让混合研究设计具备方法学可执行性和结论边界意识。
- **实施路径**：
  - 扩展 `references/claim-evidence-matrix.md`，明确不同结论需要何种证据支持。
  - 扩展 `references/indicator-system.md`，细化指标来源、专家咨询、Delphi、AHP、熵权法、信效度检验的适用边界。
  - 扩展 `references/quantitative-methods.md`，补充问卷、准实验、学习分析、日志数据、EFA/CFA、结构方程模型的最低报告要求。
  - 扩展 `references/qualitative-methods.md`，补充访谈、焦点小组、课堂观察、政策文本分析、编码一致性要求。
  - 扩展 `references/triangulation.md`，形成“研究问题 -> 量化证据 -> 质性证据 -> 系统证据 -> 结论边界”模板。
  - 增加 `references/method-reporting-templates.md` 的填充样例。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/mixed-methods-evidence-template/references/claim-evidence-matrix.md`
  - `plugins/ed-phd-copilot/skills/mixed-methods-evidence-template/references/indicator-system.md`
  - `plugins/ed-phd-copilot/skills/mixed-methods-evidence-template/references/quantitative-methods.md`
  - `plugins/ed-phd-copilot/skills/mixed-methods-evidence-template/references/qualitative-methods.md`
  - `plugins/ed-phd-copilot/skills/mixed-methods-evidence-template/references/triangulation.md`
  - `plugins/ed-phd-copilot/skills/mixed-methods-evidence-template/references/method-reporting-templates.md`
- **验收标准**：
  - 技能能识别“用模型准确率证明教育治理效果”“用满意度证明学习成效”“无对照组声称因果效果”等证据错配。
  - 技能能明确哪些结论需要降级、补证据或重设研究设计。

### 3.6 完善 `governance-figure-designer` 参考体系

- **目标**：让图示设计能够服务教育信息化治理论文中的复杂机制表达。
- **实施路径**：
  - 扩展 `references/figure-types.md`，覆盖宏观治理框架图、分层架构图、多主体协同图、人智循环图、指标体系图、证据链图、研究设计流程图。
  - 扩展 `references/layout-patterns.md`，补充金字塔、泳道图、闭环反馈图、矩阵图、同心圆、双轨架构图等布局规则。
  - 扩展 `references/label-language.md`，把工程化表达转换为教育治理表达。
  - 扩展 `references/quality-audit.md`，加入图题、图注、变量命名、责任边界、人类监督、数据流向和反馈机制审查。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/governance-figure-designer/references/figure-types.md`
  - `plugins/ed-phd-copilot/skills/governance-figure-designer/references/layout-patterns.md`
  - `plugins/ed-phd-copilot/skills/governance-figure-designer/references/label-language.md`
  - `plugins/ed-phd-copilot/skills/governance-figure-designer/references/quality-audit.md`
- **验收标准**：
  - 用户描述图意后，技能能输出可交给 PPT、Figma 或绘图工具执行的布局说明。
  - 图示建议必须体现主体、责任、数据、技术、制度和反馈机制。

### 3.7 完善 `edtech-pre-submission-reviewer` 参考体系

- **目标**：让投稿前审查具备教育技术期刊审稿人的严厉度和可执行性。
- **实施路径**：
  - 扩展 `references/review-rubric.md`，明确 CRITICAL、MAJOR、MINOR 的判定锚点。
  - 扩展 `references/theory-policy-checklist.md`，检查政策口号化、理论装饰化、概念堆砌、问题意识不足。
  - 扩展 `references/method-evidence-checklist.md`，检查研究问题、数据、方法、结论之间的匹配。
  - 扩展 `references/ethics-data-governance.md`，检查知情同意、数据脱敏、学生隐私、算法公平、人类复核。
  - 扩展 `references/style-anti-patterns.md`，列出 AI 腔、技术崇拜、过度赋能、结论越界、中文学术表达松散等问题。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/edtech-pre-submission-reviewer/references/review-rubric.md`
  - `plugins/ed-phd-copilot/skills/edtech-pre-submission-reviewer/references/theory-policy-checklist.md`
  - `plugins/ed-phd-copilot/skills/edtech-pre-submission-reviewer/references/method-evidence-checklist.md`
  - `plugins/ed-phd-copilot/skills/edtech-pre-submission-reviewer/references/ethics-data-governance.md`
  - `plugins/ed-phd-copilot/skills/edtech-pre-submission-reviewer/references/style-anti-patterns.md`
- **验收标准**：
  - 审查输出按严重性排序。
  - 每条问题都包含定位、问题原因、修改建议和 72 小时内可执行动作。

### 3.8 完善 `ai-assisted-edtech-research-workflow` 参考体系

- **目标**：明确 AI 辅助教育技术研究的边界、流程、合规规则和验证机制。
- **实施路径**：
  - 扩展 `references/human-ai-boundary.md`，明确研究者必须保留的判断权、解释权和责任权。
  - 扩展 `references/allowed-uses.md`，列出文献整理、提纲生成、语言润色、图示建议、代码辅助、数据清洗辅助等可用场景。
  - 扩展 `references/red-lines.md`，列出伪造引用、伪造数据、替代核心判断、隐藏 AI 使用、泄露敏感数据等红线。
  - 扩展 `references/verification-checklist.md`，要求每次 AI 产出进行来源、证据、引用、方法和伦理验证。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/ai-assisted-edtech-research-workflow/references/human-ai-boundary.md`
  - `plugins/ed-phd-copilot/skills/ai-assisted-edtech-research-workflow/references/allowed-uses.md`
  - `plugins/ed-phd-copilot/skills/ai-assisted-edtech-research-workflow/references/red-lines.md`
  - `plugins/ed-phd-copilot/skills/ai-assisted-edtech-research-workflow/references/verification-checklist.md`
- **验收标准**：
  - 技能能输出清晰的人机分工表。
  - 面对不合规请求时，技能能警示、拒绝或改写为合规路径。

## 四、优先级二：强化三个核心技能

### 4.1 核心技能一：强化 `governance-idea-evaluator`

- **目标**：让它成为所有研究任务进入技能链的第一道质量闸门。
- **实施路径**：
  - 在 `SKILL.md` 中明确执行顺序：先检查致命缺陷，再评分，再给出路由。
  - 增加短路规则：出现 CRITICAL 风险时，不输出装饰性高分。
  - 增加选题成熟度分级：萌芽选题、可开题选题、可投稿选题、可博士论文拓展选题。
  - 增加下一步路由：进入论文模板、证据设计、引言起草、AI 辅助研究流程或建议回到选题重构。
  - 建立“选题重构模板”，把低质量选题改写为治理问题导向选题。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/governance-idea-evaluator/SKILL.md`
  - `plugins/ed-phd-copilot/skills/governance-idea-evaluator/references/rubric.md`
  - `plugins/ed-phd-copilot/skills/governance-idea-evaluator/references/fatal-flaws.md`
  - `docs/examples/failure-cases/`
- **验收标准**：
  - 同一选题多次执行，结论稳定。
  - 输出能清楚说明“为什么通过、为什么转向、下一步进入哪个技能”。

### 4.2 核心技能二：强化 `governance-paper-template`

- **目标**：让它成为系统、机制、框架和治理类论文的主编排器。
- **实施路径**：
  - 将论文类型进一步细化为治理机制型、系统架构型、指标体系型、设计科学型、政策分析型、案例研究型。
  - 为每类论文提供章节骨架、关键论点、证据需求和常见失败模式。
  - 强制输出“理论 -> 机制 -> 系统 -> 证据 -> 贡献”五列表。
  - 增加“实践进路生成规则”：观念更新、机制重塑、评价升级、伦理规约四维必须与前文问题对应。
  - 增加“博士论文拓展路径”：把一篇论文型结构扩展为博士论文的章节群。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/governance-paper-template/SKILL.md`
  - `plugins/ed-phd-copilot/skills/governance-paper-template/references/paper-types.md`
  - `plugins/ed-phd-copilot/skills/governance-paper-template/references/section-skeleton.md`
  - `plugins/ed-phd-copilot/skills/governance-paper-template/references/theory-to-design.md`
- **验收标准**：
  - 输出的论文骨架能直接用于开题报告或论文大纲。
  - 每个章节都能说明其功能、论点、证据和与总问题的关系。

### 4.3 核心技能三：强化 `mixed-methods-evidence-template`

- **目标**：让它成为教育技术实证研究和混合研究的证据设计核心。
- **实施路径**：
  - 建立“研究问题 -> 变量/指标 -> 数据来源 -> 分析方法 -> 可支持结论”矩阵。
  - 明确 Delphi、AHP、EFA、CFA、准实验、访谈、日志分析、政策文本分析的适用条件。
  - 增加“结论边界控制”规则：没有追踪数据不得声称长期影响；没有对照组不得强因果；只有满意度不得声称学习成效。
  - 增加伦理审查前置步骤。
  - 增加对“教育治理效果”的多源证据要求，例如制度变化、行为变化、流程变化、组织协同变化、数据质量变化。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/mixed-methods-evidence-template/SKILL.md`
  - `plugins/ed-phd-copilot/skills/mixed-methods-evidence-template/references/claim-evidence-matrix.md`
  - `plugins/ed-phd-copilot/skills/mixed-methods-evidence-template/references/triangulation.md`
  - `plugins/ed-phd-copilot/skills/mixed-methods-evidence-template/references/method-reporting-templates.md`
- **验收标准**：
  - 技能能把研究问题转化为可执行的数据收集和分析方案。
  - 技能能指出当前证据不能支持哪些结论。

### 4.4 建立核心技能之间的路由协议

- **目标**：让三个核心技能形成连续工作流，而不是孤立工具。
- **实施路径**：
  - 在 `governance-idea-evaluator` 输出中加入 `Next Skill` 字段。
  - 在 `governance-paper-template` 输出中加入 `Evidence Design Needed` 字段。
  - 在 `mixed-methods-evidence-template` 输出中加入 `Paper Section Impact` 字段。
  - 在 3 个技能的 `SKILL.md` 中统一这些字段名称。
- **产物路径**：
  - `plugins/ed-phd-copilot/skills/governance-idea-evaluator/SKILL.md`
  - `plugins/ed-phd-copilot/skills/governance-paper-template/SKILL.md`
  - `plugins/ed-phd-copilot/skills/mixed-methods-evidence-template/SKILL.md`
  - `docs/examples/`
- **验收标准**：
  - 同一研究主题可以自然完成“选题评估 -> 论文骨架 -> 证据设计”的连续输出。
  - 示例输出之间没有概念漂移和方法冲突。

## 五、优先级三：建立贯穿式真实样例

### 5.1 保留并扩展当前贯穿案例

- **目标**：继续使用“基于多 Agent 的高校智能校园治理机制研究”作为主回归案例。
- **实施路径**：
  - 检查 `docs/case-multi-agent-smart-campus.md` 是否包含研究背景、核心问题、技术设想、治理场景、利益相关者、理论基础、方法计划和伦理风险。
  - 将案例中的技术描述进一步治理化，避免变成单纯系统开发方案。
  - 标注该案例只是技能测试样例，不是最终论文文本。
- **产物路径**：
  - `docs/case-multi-agent-smart-campus.md`
- **验收标准**：
  - 7 个技能都能基于该案例独立执行。
  - 案例信息足够支撑选题、论文、方法、图示、审查和 AI 工作流输出。

### 5.2 建立第二个贯穿案例：教师数字胜任力治理

- **目标**：增加一个偏教师发展和组织支持的教育技术治理样例。
- **实施路径**：
  - 新建案例文件，主题可设为“区域中小学教师数字胜任力提升的组织支持机制研究”。
  - 写明政策背景、教师发展痛点、学校/区域管理机制、数据收集方案、伦理问题。
  - 用 7 个技能分别跑一遍，并保存输出。
- **产物路径**：
  - `docs/cases/case-teacher-digital-competence-governance.md`
  - `docs/examples/case-teacher-digital-competence/`
- **验收标准**：
  - 该案例能检验技能是否适用于“非智能校园、非多 Agent”的教育治理主题。
  - 输出能体现教师主体性、组织支持和专业发展逻辑。

### 5.3 建立第三个贯穿案例：教育数据治理

- **目标**：增加一个偏数据治理、隐私保护和制度设计的样例。
- **实施路径**：
  - 新建案例文件，主题可设为“高校教育数据治理能力建设与风险防控机制研究”。
  - 写明数据来源、数据权责、治理流程、隐私风险、质量控制和组织协同问题。
  - 用 7 个技能生成完整示例输出。
- **产物路径**：
  - `docs/cases/case-education-data-governance.md`
  - `docs/examples/case-education-data-governance/`
- **验收标准**：
  - 该案例能检验技能对数据伦理、数据质量、制度责任和算法治理的处理能力。
  - 投稿前审查技能能识别数据治理相关风险。

### 5.4 建立第四个贯穿案例：人机协同评价

- **目标**：增加一个偏教学评价、学习分析和人机协同决策的样例。
- **实施路径**：
  - 新建案例文件，主题可设为“人机协同支持的课堂教学评价改进机制研究”。
  - 写明评价主体、评价指标、AI 辅助角色、教师复核机制、学生数据权益。
  - 用核心三个技能先跑通，再扩展到 7 个技能。
- **产物路径**：
  - `docs/cases/case-human-ai-assessment-governance.md`
  - `docs/examples/case-human-ai-assessment/`
- **验收标准**：
  - 该案例能检验技能是否能处理评价异化、算法黑箱和教师专业判断之间的关系。
  - 证据设计必须区分评价效率、评价质量、教师采纳和学生学习成效。

### 5.5 建立样例输出规范

- **目标**：让所有样例输出可比较、可复用、可回归测试。
- **实施路径**：
  - 为每个样例输出统一加入输入摘要、调用技能、使用 reference、主要输出、质量自查、遗留问题。
  - 将旧有 `docs/examples/01-...` 至 `07-...` 按此格式补齐。
  - 新增案例输出时沿用同一格式。
- **产物路径**：
  - `docs/examples/README.md`
  - `docs/examples/01-governance-idea-evaluator-output.md`
  - `docs/examples/02-governance-paper-template-output.md`
  - `docs/examples/03-edtech-intro-drafter-output.md`
  - `docs/examples/04-mixed-methods-evidence-output.md`
  - `docs/examples/05-governance-figure-designer-output.md`
  - `docs/examples/06-edtech-pre-submission-review-output.md`
  - `docs/examples/07-ai-assisted-workflow-output.md`
- **验收标准**：
  - 所有样例都能追溯到输入、技能、reference 和质量检查。
  - 新读者能把样例当作使用说明和质量标准。

### 5.6 建立失败案例回归测试

- **目标**：确保技能不只会生成好看的输出，也能识别坏输入和错误研究设计。
- **实施路径**：
  - 保留现有失败案例目录。
  - 增加失败类型：技术先行、政策口号化、证据错配、理论装饰化、伦理缺位、结论越界、AI 伪引用。
  - 每个失败案例包含输入、期望识别的问题、期望输出的警示级别和修复建议。
  - 后续修改技能后，重新运行失败案例并记录结果。
- **产物路径**：
  - `docs/examples/failure-cases/README.md`
  - `docs/examples/failure-cases/*.md`
- **验收标准**：
  - 核心技能能稳定识别 CRITICAL 问题。
  - 失败案例不会被技能误判为高质量研究设计。

## 六、文献与证据体系完善任务

### 6.1 核验中文核心/CSSCI 候选文献

- **目标**：把候选文献从“检索目标”升级为“可引用证据”。
- **实施路径**：
  - 从 `docs/chinese-core-literature-inventory.md` 中筛选 `needs_cnki_verification` 条目。
  - 通过 CNKI、期刊官网、本地 PDF 或学校数据库核验题名、作者、来源、年份、卷期、页码、DOI。
  - 核验成功后写入新的正式题录文件。
  - 未核验条目继续保留为候选，不进入正式引用。
- **产物路径**：
  - `docs/chinese-core-literature-inventory.md`
  - `docs/chinese-core-literature-verified.md`
  - `docs/verified-source-registry.md`
- **验收标准**：
  - 每条正式引用都有可追溯来源。
  - 未核验文献不出现在正式参考文献或技能依据中。

### 6.2 建立教育信息化治理主题文献地图

- **目标**：让 references 的理论和方法依据更系统。
- **实施路径**：
  - 以主题分类整理文献：教育数字化转型、教育数据治理、智能校园治理、教师数字素养、AI 教育治理、学习分析伦理、教育领导力、组织变革。
  - 每个主题提炼核心概念、可用理论、常见方法、代表性争议。
  - 将主题地图反向链接到对应技能。
- **产物路径**：
  - `docs/literature-map-edtech-governance.md`
  - `docs/evidence-base.md`
- **验收标准**：
  - 每个核心技能至少能对应 3 类文献主题。
  - 文献地图能指导选题、论文结构和方法设计。

### 6.3 建立方法学证据登记表

- **目标**：区分政策依据、理论依据、方法依据、案例依据和伦理依据。
- **实施路径**：
  - 在 `docs/evidence-base.md` 中建立来源类型字段。
  - 对每个技能标注主要依据类型。
  - 对方法类 reference 标注最低报告标准来自何种方法学传统。
- **产物路径**：
  - `docs/evidence-base.md`
  - `docs/verified-source-registry.md`
- **验收标准**：
  - 技能依据不会混淆政策文件、理论文献和方法教材。
  - 审查时能看出某条规则来自哪类证据。

## 七、仓库级质量控制任务

### 7.1 强化结构检查脚本

- **目标**：把人工检查转为可重复的结构检查。
- **实施路径**：
  - 扩展 `scripts/check_skill_structure.py`，检查每个技能是否存在 `SKILL.md`、`agents/openai.yaml`、`references/`。
  - 检查每个 `SKILL.md` 是否包含 `name` 和 `description`。
  - 检查是否存在空 reference、明显 TODO、placeholder。
  - 检查关键文档是否存在：README、NOTICE、LICENSE、evidence-base、coverage matrix、install-readiness audit。
  - 输出 PASS/FAIL 和具体缺失路径。
- **产物路径**：
  - `scripts/check_skill_structure.py`
- **验收标准**：
  - 一条命令能输出结构检查结果。
  - 检查失败时能定位到具体文件。

### 7.2 建立内容覆盖矩阵维护规则

- **目标**：持续追踪每个技能的完整度。
- **实施路径**：
  - 更新 `docs/skill-coverage-matrix.md`。
  - 覆盖字段至少包括 rubric、checklist、anti-patterns、worked example、method detail、ethics check、routing rule、failure cases。
  - 每新增一个 reference 或 example，就同步更新矩阵。
- **产物路径**：
  - `docs/skill-coverage-matrix.md`
- **验收标准**：
  - 能一眼看出哪个技能仍薄弱。
  - 矩阵状态与实际文件一致。

### 7.3 建立版本发布流程

- **目标**：避免仓库内容、README 和版本记录不一致。
- **实施路径**：
  - 每次完成一个迭代批次后更新 `CHANGELOG.md`。
  - 每次进入新成熟度等级后更新 README 的“当前成熟度”。
  - 每次发布前运行结构检查脚本。
  - 每次发布前检查 `git status`，确认没有遗漏文件。
- **产物路径**：
  - `CHANGELOG.md`
  - `README.md`
  - `docs/install-readiness-audit.md`
- **验收标准**：
  - 版本记录、README、审计文件和实际文件状态一致。
  - GitHub 上的默认分支包含完整版本内容。

### 7.4 建立安装后前向测试

- **目标**：确认技能不是只在仓库内结构正确，而是在安装后能够被 Codex 正确触发和使用。
- **实施路径**：
  - 安装到本地技能目录前，保留当前仓库作为源项目。
  - 安装后分别用 7 个典型提示词触发技能。
  - 记录每个技能是否正确触发、是否按 reference 读取、是否输出合规格式。
  - 把测试结果写入安装后测试报告。
- **产物路径**：
  - `docs/install-forward-test.md`
- **验收标准**：
  - 7 个技能均能被正确触发。
  - 输出不泄露无关模板，不跳过必要的核验和伦理边界。

## 八、建议实施顺序

### 8.1 第一轮：references 精修

1. 核对 7 个技能的 `references/` 是否完整。
2. 为每个 reference 增加“用途、适用情境、输出影响”。
3. 删除或合并重复解释。
4. 更新 `docs/skill-coverage-matrix.md`。
5. 运行结构检查脚本。

### 8.2 第二轮：核心技能增强

1. 强化 `governance-idea-evaluator` 的短路规则和路由输出。
2. 强化 `governance-paper-template` 的论文类型和章节骨架。
3. 强化 `mixed-methods-evidence-template` 的证据矩阵和结论边界。
4. 用主贯穿案例跑通三技能链。
5. 根据输出问题反向修订 references。

### 8.3 第三轮：多案例回归

1. 保留智能校园治理案例作为主案例。
2. 增加教师数字胜任力治理案例。
3. 增加教育数据治理案例。
4. 增加人机协同评价案例。
5. 每个案例至少跑通三个核心技能。
6. 每个案例至少生成一份失败输入和对应审查结果。

### 8.4 第四轮：文献证据核验

1. 从中文核心文献 inventory 中筛选最高优先级条目。
2. 核验题录信息。
3. 写入正式 verified bibliography。
4. 将核验文献映射到对应技能和 reference。
5. 更新 evidence base。

### 8.5 第五轮：发布与安装测试

1. 更新 README、CHANGELOG、coverage matrix 和 install audit。
2. 运行结构检查脚本。
3. 推送到 GitHub。
4. 本地安装测试。
5. 记录安装后前向测试报告。

## 九、完成度分级

| 等级 | 标准 | 对应状态 |
|---|---|---|
| V0.1 初版 | 已有技能雏形，方向正确，但 reference 和案例不足 | 已完成 |
| V0.2 结构增强版 | 每个技能有基础 reference、rubric 或 checklist | 已完成 |
| V0.3 方法增强版 | 三个核心技能具备评分、模板和证据链规则 | 已完成 |
| V0.4 样例验证版 | 贯穿案例跑通 7 个技能并保存示例输出 | 已完成 |
| V0.5 回归增强版 | 增加失败案例、方法模板和文献地图 | 已完成 |
| V0.6 文献增强版 | 建立中文核心文献 inventory 和方法填充样例 | 已完成 |
| V1.0 安装前可用版 | README、导读、references、案例、检查脚本、审计文件齐全 | 当前基线 |
| V1.1 多案例验证版 | 至少 4 个教育技术治理场景完成核心技能回归测试 | 下一阶段目标 |
| V1.2 文献核验版 | 建立正式中文核心/CSSCI verified bibliography | 下一阶段目标 |
| V1.3 安装后稳定版 | 本地安装后 7 个技能均完成前向测试 | 下一阶段目标 |
| V2.0 博士研究工作台版 | 支持从选题、开题、研究设计、写作、图示到投稿审查的完整闭环 | 长期目标 |

## 十、下一步最小可执行任务

如果只执行一轮最小改进，建议按以下顺序推进：

1. 新建 `docs/cases/`，加入教师数字胜任力治理、教育数据治理、人机协同评价 3 个案例草案。
2. 用三个核心技能分别测试 3 个新案例，保存到 `docs/examples/case-*/`。
3. 扩展 `docs/examples/failure-cases/`，每个新案例至少加入 1 个失败输入。
4. 更新 `docs/skill-coverage-matrix.md`，加入 failure cases 字段。
5. 从 `docs/chinese-core-literature-inventory.md` 中核验 5 条最高价值中文文献，写入 `docs/chinese-core-literature-verified.md`。
6. 更新 `docs/evidence-base.md` 和 `docs/verified-source-registry.md`。
7. 运行 `scripts/check_skill_structure.py`。
8. 更新 `CHANGELOG.md`，标记为 V1.1 或 V1.2 的阶段性进展。
