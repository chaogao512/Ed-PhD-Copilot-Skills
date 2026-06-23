# Ed-PdD-Copilot-Skills 逐步完善任务清单

> 目标：将当前 `Ed-PdD-Copilot-Skills` 从“方向正确的初版技能集”升级为“具有教育技术学术深度、教育信息化治理专业适配度、可复用执行规范和可验证案例支撑”的成熟技能库。  
> 参照对象：`Supervisor-Skills` 的完整度、分层结构、参考文件体系、评分规则、反例库、示例输出和可执行检查表。  
> 优先级来源：当前评审结论中的三个优先级：补齐 `references/`、强化核心技能、建立贯穿样例。

## 一、总体工作原则

### 1.1 保持 Skill 主文件精炼

- **目标**：每个 `SKILL.md` 只保留触发说明、核心流程、引用入口和输出格式。
- **实施路径**：
  - 检查 7 个 `SKILL.md` 是否存在过长解释。
  - 将评分细则、案例、反例、术语表、方法细节移入 `references/`。
  - 在 `SKILL.md` 中以“何时读取哪个 reference”的方式建立导航。
- **验收标准**：
  - 每个 `SKILL.md` 不超过 180 行。
  - 每个核心流程节点至少指向一个可选 reference。
  - 无大段重复解释。

### 1.2 所有判断都要有锚点

- **目标**：避免 AI 凭直觉打分或泛泛建议。
- **实施路径**：
  - 为评分项建立 1/3/5 或 CRITICAL/MAJOR/MINOR 锚点。
  - 为“通过、需修订、转向”建立明确判定条件。
  - 对常见失败模式给出检测规则。
- **验收标准**：
  - 每个评估类技能至少有一个 `rubric.md`。
  - 每个审查类技能至少有一个 `checklist.md` 或 `anti-patterns.md`。

### 1.3 所有技能都要能落到教育技术真实场景

- **目标**：避免技能停留在概念层。
- **实施路径**：
  - 统一采用一个贯穿案例：“基于多 Agent 的高校智能校园治理机制研究”。
  - 每个技能提供至少一个该案例的 worked example。
  - 每个技能补充至少两个可替换场景：教师数字胜任力、教育数据治理、人机协同评价、区域教育数字化治理。
- **验收标准**：
  - 每个技能至少有 1 个完整 worked example。
  - 技能输出能体现“政策-组织-技术-人-证据-伦理”的综合逻辑。

## 二、优先级一：补齐 references 支撑体系

### 2.1 为 `governance-idea-evaluator` 补齐参考文件

- **目标**：使选题评估从“维度列表”升级为“可复核评分系统”。
- **实施路径**：
  - 新建 `plugins/ed-pdd-copilot/skills/governance-idea-evaluator/references/rubric.md`。
  - 定义 7 个评分维度的 1/3/5 分锚点：政策相关性、教育价值、组织可行性、人智协同、方法可证性、伦理可控性、理论贡献。
  - 新建 `fatal-flaws.md`，扩展当前 6 个致命缺陷，加入检测问题、严重性、修复策略。
  - 新建 `theory-anchors.md`，说明协同治理、组织变革、社会技术系统、活动理论、TPACK、PDCA、数据治理理论等如何进入研究设计。
  - 新建 `worked-examples.md`，用 3 个选题演示评估过程。
- **验收标准**：
  - 能对一个博士选题输出总分、短板、红线风险和推进建议。
  - 出现 CRITICAL 时能短路，不继续做装饰性评分。

### 2.2 为 `edtech-intro-drafter` 补齐参考文件

- **目标**：使引言技能具备教育技术顶刊写作范式，而不是只给段落标题。
- **实施路径**：
  - 新建 `references/four-part-logic.md`，细化“政策背景-技术赋能-现实异化-研究合法性”四重奏。
  - 新建 `references/paragraph-patterns.md`，为六段式引言提供段落功能、写作要点、常见句式和错误示例。
  - 新建 `references/alienation-patterns.md`，整理数字形式主义、数据孤岛、教师数字倦怠、算法黑箱、评价异化等典型矛盾。
  - 新建 `references/worked-examples.md`，用“多 Agent 智能校园治理”生成一份完整引言大纲。
- **验收标准**：
  - 输出不再是泛泛大纲，而能形成可直接扩写的段落骨架。
  - 每段都能说明其学术功能和需要补充的证据。

### 2.3 为 `governance-paper-template` 补齐参考文件

- **目标**：使系统/机制类论文模板能够支撑博士论文和 CSSCI/SSCI 稿件结构。
- **实施路径**：
  - 新建 `references/paper-types.md`，定义治理框架、智能校园架构、人智协同机制、设计科学研究、指标体系、组织变革六类论文。
  - 新建 `references/theory-to-design.md`，建立“理论概念-设计原则-系统模块-证据指标”的映射表。
  - 新建 `references/dual-topology.md`，细化基础设施层、数据治理层、智能协同层、业务应用层、人类监督层。
  - 新建 `references/section-skeleton.md`，给出系统架构与机制阐释论文的章节结构。
  - 新建 `references/worked-examples.md`，用一个完整案例填充论文骨架。
- **验收标准**：
  - 用户给出一个研究设想后，技能能输出章节级论文结构。
  - 每个技术模块都能追溯到理论依据和治理问题。

### 2.4 为 `mixed-methods-evidence-template` 补齐参考文件

- **目标**：使混合研究设计具备方法学可执行性。
- **实施路径**：
  - 新建 `references/claim-evidence-matrix.md`，列出不同结论类型需要的证据类型。
  - 新建 `references/indicator-system.md`，规范指标来源、文献编码、专家咨询、Delphi、AHP/熵权法使用条件。
  - 新建 `references/quantitative-methods.md`，说明问卷、准实验、日志数据、EFA/CFA、信效度检验的最低报告要求。
  - 新建 `references/qualitative-methods.md`，说明访谈、焦点小组、观察、文本分析、编码一致性的最低报告要求。
  - 新建 `references/triangulation.md`，建立“研究问题-量化证据-质性证据-系统证据-结论边界”的矩阵模板。
- **验收标准**：
  - 技能能识别“用模型准确率证明教育效果”这类证据错配。
  - 技能能明确哪些结论必须降级或补证据。

### 2.5 为 `governance-figure-designer` 补齐参考文件

- **目标**：使图示技能能指导教育技术论文中的系统图、机制图、模型图和证据链图。
- **实施路径**：
  - 新建 `references/figure-types.md`，定义宏观治理框架图、分层架构图、多主体协同图、人智循环图、指标体系图、证据链图。
  - 新建 `references/layout-patterns.md`，给出金字塔、同心圆、泳道图、矩阵图、闭环反馈图等布局规则。
  - 新建 `references/label-language.md`，提供工程词汇到教育治理词汇的替换表。
  - 新建 `references/quality-audit.md`，建立图表质量审查清单。
  - 新建 `references/worked-examples.md`，给出一个“智能校园治理架构图”的文本布局样例。
- **验收标准**：
  - 用户描述图意后，技能能输出可交给 PPT/Figma/绘图工具执行的布局说明。
  - 图示建议中必须包含人类监督、责任边界和反馈机制。

### 2.6 为 `edtech-pre-submission-reviewer` 补齐参考文件

- **目标**：使投稿前审查从“问题清单”升级为“教育技术期刊审稿视角”。
- **实施路径**：
  - 新建 `references/review-rubric.md`，定义 CRITICAL/MAJOR/MINOR 的判断锚点。
  - 新建 `references/theory-policy-checklist.md`，检查政策口号化、理论装饰化、概念堆砌。
  - 新建 `references/method-evidence-checklist.md`，检查方法、数据、结论是否匹配。
  - 新建 `references/ethics-data-governance.md`，检查知情同意、数据脱敏、学生隐私、算法公平、人类复核。
  - 新建 `references/style-anti-patterns.md`，列出 AI 腔、技术崇拜、过度赋能、结论越界等表达问题。
- **验收标准**：
  - 审查输出能按严重性排序。
  - 每条问题必须包含定位、原因、修改建议和 72 小时内可执行性。

### 2.7 为 `ai-assisted-edtech-research-workflow` 补齐参考文件

- **目标**：明确 AI 辅助教育技术研究的边界、流程和验证机制。
- **实施路径**：
  - 新建 `references/human-ai-boundary.md`，定义研究者必须保留的判断权。
  - 新建 `references/allowed-uses.md`，列出文献整理、提纲生成、语言润色、图示建议、代码辅助等可用场景。
  - 新建 `references/red-lines.md`，列出伪造引用、伪造数据、替代核心判断、隐藏 AI 使用等红线。
  - 新建 `references/verification-checklist.md`，要求每次 AI 产出进行来源、证据、引用、方法、伦理验证。
- **验收标准**：
  - 技能能给出具体的人机分工表。
  - 技能能拒绝或警示不合规请求。

## 三、优先级二：强化三个核心技能

### 3.1 强化 `governance-idea-evaluator`

- **目标**：让它成为所有研究任务的入口闸门。
- **实施路径**：
  - 在 `SKILL.md` 中加入“先读取 `references/fatal-flaws.md`，再读取 `references/rubric.md`”的执行顺序。
  - 增加短路规则：只要出现伦理不可控、证据错配、理论真空、技术先行无治理问题中的 CRITICAL，就输出 `Pivot`。
  - 增加“选题成熟度分级”：萌芽选题、可开题选题、可投稿选题、可博士论文拓展选题。
  - 增加“下一步路由”：通过后路由到 `governance-paper-template` 或 `mixed-methods-evidence-template`。
- **验收标准**：
  - 对同一选题多次执行，结论稳定。
  - 输出能直接指导下一步进入哪个技能。

### 3.2 强化 `governance-paper-template`

- **目标**：让它成为系统/机制/框架类论文的主编排器。
- **实施路径**：
  - 将六类论文类型细化为不同章节结构。
  - 强制输出“理论-机制-系统-证据”四列表。
  - 增加“贡献声明检查”：理论贡献、方法贡献、实践贡献、政策启示不能混淆。
  - 增加“实践进路生成规则”：观念更新、机制重塑、评价升级、伦理规约四维必须与前文问题对应。
- **验收标准**：
  - 输出的论文骨架能直接用于开题报告或论文大纲。
  - 每个章节都有功能说明、关键论点和所需证据。

### 3.3 强化 `mixed-methods-evidence-template`

- **目标**：让它成为教育技术实证与混合研究的证据设计核心。
- **实施路径**：
  - 建立“研究问题-变量/指标-数据来源-分析方法-可支持结论”矩阵。
  - 明确 Delphi、AHP、EFA、CFA、准实验、访谈、日志分析的适用条件和常见误用。
  - 增加“结论边界控制”规则：没有追踪数据不得声称长期影响；没有对照组不得强因果；只有满意度不得声称学习成效。
  - 增加“伦理审查前置”步骤。
- **验收标准**：
  - 能帮助用户把研究问题转化为可执行的数据收集方案。
  - 能明确指出哪些结论当前证据不能支持。

## 四、优先级三：建立贯穿式真实样例

### 4.1 确定贯穿案例

- **目标**：用同一个案例测试 7 个技能的一致性。
- **建议案例**：基于多 Agent 的高校智能校园治理机制研究。
- **实施路径**：
  - 新建 `docs/case-multi-agent-smart-campus.md`。
  - 写明研究背景、核心问题、技术设想、治理场景、利益相关者、拟用理论、拟用方法。
  - 明确该案例不是最终论文，只是技能测试样例。
- **验收标准**：
  - 案例信息足够让 7 个技能分别执行。

### 4.2 用案例测试 `governance-idea-evaluator`

- **目标**：检验选题评估技能是否能发现问题、给出推进建议。
- **实施路径**：
  - 将案例输入技能。
  - 保存输出到 `docs/examples/01-governance-idea-evaluator-output.md`。
  - 标注技能输出是否覆盖政策、组织、伦理、理论、证据。
- **验收标准**：
  - 输出包含评分表、红线风险、理论建议和下一步路由。

### 4.3 用案例测试 `governance-paper-template`

- **目标**：检验论文骨架技能是否能生成结构化大纲。
- **实施路径**：
  - 使用同一案例生成论文类型判断、章节结构、理论-机制-系统-证据矩阵。
  - 保存输出到 `docs/examples/02-governance-paper-template-output.md`。
- **验收标准**：
  - 输出能直接改写为开题报告或论文大纲。

### 4.4 用案例测试 `edtech-intro-drafter`

- **目标**：检验引言技能是否能形成顶刊式论证链。
- **实施路径**：
  - 使用同一案例生成六段式引言大纲。
  - 保存输出到 `docs/examples/03-edtech-intro-drafter-output.md`。
  - 检查是否包含政策背景、技术赋能、现实异化、理论桥接和贡献。
- **验收标准**：
  - 每段都有功能、论点、证据需求和风险提示。

### 4.5 用案例测试 `mixed-methods-evidence-template`

- **目标**：检验证据设计技能是否能形成可执行研究方案。
- **实施路径**：
  - 为案例设计问卷、访谈、日志数据、专家论证、治理过程指标。
  - 保存输出到 `docs/examples/04-mixed-methods-evidence-output.md`。
- **验收标准**：
  - 输出包含研究问题-证据-方法-结论边界矩阵。

### 4.6 用案例测试 `governance-figure-designer`

- **目标**：检验图示技能是否能输出可绘制的图结构。
- **实施路径**：
  - 为案例设计“多 Agent 智能校园治理架构图”和“人智协同反馈机制图”。
  - 保存输出到 `docs/examples/05-governance-figure-designer-output.md`。
- **验收标准**：
  - 输出包含布局、元素、箭头类型、图注和质量审查。

### 4.7 用案例测试 `edtech-pre-submission-reviewer`

- **目标**：检验审稿技能是否能发现教育技术论文的关键风险。
- **实施路径**：
  - 构造一份 800-1200 字的案例论文摘要或引言草稿。
  - 让技能进行投稿前审查。
  - 保存输出到 `docs/examples/06-edtech-pre-submission-review-output.md`。
- **验收标准**：
  - 输出按 CRITICAL/MAJOR/MINOR 排序，并给出 72 小时修订计划。

### 4.8 用案例测试 `ai-assisted-edtech-research-workflow`

- **目标**：检验 AI 辅助研究流程技能是否能划清人机边界。
- **实施路径**：
  - 以“准备开题报告的一周工作”为情境。
  - 输出人机分工表、AI 可辅助任务、禁止事项、验证清单。
  - 保存到 `docs/examples/07-ai-assisted-workflow-output.md`。
- **验收标准**：
  - 输出明确哪些判断必须由研究者负责。

## 五、仓库级质量控制任务

### 5.1 建立结构检查脚本

- **目标**：避免新增技能或 reference 后结构混乱。
- **实施路径**：
  - 新建 `scripts/check_skill_structure.py`。
  - 检查每个 skill 是否有 `SKILL.md`、`agents/openai.yaml`、`references/`。
  - 检查 `SKILL.md` 是否有 `name` 和 `description`。
  - 检查是否存在 `TODO`、`placeholder`、空 reference 文件。
- **验收标准**：
  - 一条命令能输出结构检查结果。

### 5.2 建立内容覆盖矩阵

- **目标**：追踪每个技能的完整度。
- **实施路径**：
  - 新建 `docs/skill-coverage-matrix.md`。
  - 列出 7 个技能和以下字段：rubric、checklist、anti-patterns、worked-example、method detail、ethics check、routing rule。
  - 每次补充后更新矩阵。
- **验收标准**：
  - 能一眼看出哪个技能还薄弱。

### 5.3 更新顶层 README

- **目标**：让使用者理解技能成熟度和使用顺序。
- **实施路径**：
  - 增加“当前成熟度”章节。
  - 增加“推荐学习/使用路径”。
  - 增加“示例案例”链接。
  - 明确哪些技能已具备 worked example，哪些仍在建设。
- **验收标准**：
  - 用户打开仓库能知道从哪个技能开始。

### 5.4 更新 `plugins/ed-pdd-copilot/skills/README.md`

- **目标**：让技能导读达到 `Supervisor-Skills` 的导读水平。
- **实施路径**：
  - 为每个技能补“定位、什么时候触发、产出、上游/下游接龙、对应 references”。
  - 增加两条主线：治理机制论文主线、指标体系/混合研究主线。
  - 增加“遇到具体瓶颈时怎么选技能”。
- **验收标准**：
  - 不安装技能也能把 README 当作研究流程指南。

## 六、建议实施顺序

### 第一轮：搭好 references 骨架

1. 为 7 个技能建立 reference 文件。
2. 更新各 `SKILL.md` 的 reference 导航。
3. 建立 `docs/skill-coverage-matrix.md`。

### 第二轮：补强三大核心技能

1. 深化 `governance-idea-evaluator`。
2. 深化 `governance-paper-template`。
3. 深化 `mixed-methods-evidence-template`。

### 第三轮：补写样例并回测

1. 建立贯穿案例。
2. 用案例跑 7 个技能。
3. 根据失败输出反向修订技能。

### 第四轮：仓库级 polish

1. 更新 README 和技能导读。
2. 增加结构检查脚本。
3. 进行最终校验、提交并发布。

## 七、完成度分级

| 等级 | 标准 |
|---|---|
| V0.1 初版 | 已有 7 个 SKILL.md，方向正确，但 reference 和案例不足 |
| V0.2 结构增强版 | 每个技能有 rubric/checklist/anti-patterns 至少一种 reference |
| V0.3 方法增强版 | 三个核心技能具备完整评分、模板和证据链规则 |
| V0.4 样例验证版 | 贯穿案例跑通 7 个技能，并保存示例输出 |
| V1.0 可用版 | README、导读、references、案例、检查脚本齐全，可稳定支持博士研究任务 |

