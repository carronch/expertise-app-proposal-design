# EntreComp: the competence map

EntreComp is the European Commission's reference model of entrepreneurship as a competence for everyone. This vault uses it as a shared language for what a student is growing, and as **evidence, never a grade**.

> "Entrepreneurship is when you act upon opportunities and ideas and transform them into value for others. The value that is created can be financial, cultural, or social." (p. 10)

**Source:** Bacigalupo, M., Kampylis, P., Punie, Y., & Van den Brande, G. (2016). *EntreComp: The Entrepreneurship Competence Framework*. JRC Science for Policy Report, EUR 27939 EN. Luxembourg: Publications Office of the European Union. doi:[10.2791/593884](https://doi.org/10.2791/593884). © European Union, 2016. "Reproduction is authorised provided the source is acknowledged." Page numbers below are the report's printed pages.

## Three areas, fifteen competences (Table 1, pp. 12–13)

### 1. Ideas and opportunities

| Competence | Hint | Descriptors |
|---|---|---|
| 1.1 Spotting opportunities | Use your imagination and abilities to identify opportunities for creating value | Identify and seize opportunities to create value by exploring the social, cultural and economic landscape · Identify needs and challenges that need to be met · Establish new connections and bring together scattered elements of the landscape to create opportunities to create value |
| 1.2 Creativity | Develop creative and purposeful ideas | Develop several ideas and opportunities to create value, including better solutions to existing and new challenges · Explore and experiment with innovative approaches · Combine knowledge and resources to achieve valuable effects |
| 1.3 Vision | Work towards your vision of the future | Imagine the future · Develop a vision to turn ideas into action · Visualise future scenarios to help guide effort and action |
| 1.4 Valuing ideas | Make the most of ideas and opportunities | Judge what value is in social, cultural and economic terms · Recognise the potential an idea has for creating value and identify suitable ways of making the most out of it |
| 1.5 Ethical and sustainable thinking | Assess the consequences and impact of ideas, opportunities and actions | Assess the consequences of ideas that bring value and the effect of entrepreneurial action on the target community, the market, society and the environment · Reflect on how sustainable long-term social, cultural and economic goals are, and the course of action chosen · Act responsibly |

### 2. Resources

| Competence | Hint | Descriptors |
|---|---|---|
| 2.1 Self-awareness and self-efficacy | Believe in yourself and keep developing | Reflect on your needs, aspirations and wants in the short, medium and long term · Identify and assess your individual and group strengths and weaknesses · Believe in your ability to influence the course of events, despite uncertainty, setbacks and temporary failures |
| 2.2 Motivation and perseverance | Stay focused and don't give up | Be determined to turn ideas into action and satisfy your need to achieve · Be prepared to be patient and keep trying to achieve your long-term individual or group aims · Be resilient under pressure, adversity, and temporary failure |
| 2.3 Mobilizing resources | Gather and manage the resources you need | Get and manage the material, non-material and digital resources needed to turn ideas into action · Make the most of limited resources · Get and manage the competences needed at any stage, including technical, legal, tax and digital competences |
| 2.4 Financial and economic literacy | Develop financial and economic know how | Estimate the cost of turning an idea into a value-creating activity · Plan, put in place and evaluate financial decisions over time · Manage financing to make sure my value-creating activity can last over the long term |
| 2.5 Mobilizing others | Inspire, enthuse and get others on board | Inspire and enthuse relevant stakeholders · Get the support needed to achieve valuable outcomes · Demonstrate effective communication, persuasion, negotiation and leadership |

### 3. Into action

| Competence | Hint | Descriptors |
|---|---|---|
| 3.1 Taking the initiative | Go for it | Initiate processes that create value · Take up challenges · Act and work independently to achieve goals, stick to intentions and carry out planned tasks |
| 3.2 Planning and management | Prioritize, organize and follow-up | Set long-, medium- and short-term goals · Define priorities and action plans · Adapt to unforeseen changes |
| 3.3 Coping with uncertainty, ambiguity and risk | Make decisions dealing with uncertainty, ambiguity and risk | Make decisions when the result of that decision is uncertain, when the information available is partial or ambiguous, or when there is a risk of unintended outcomes · Within the value-creating process, include structured ways of testing ideas and prototypes from the early stages, to reduce risks of failing · Handle fast-moving situations promptly and flexibly |
| 3.4 Working with others | Team up, collaborate and network | Work together and co-operate with others to develop ideas and turn them into action · Network · Solve conflicts and face up to competition positively when necessary |
| 3.5 Learning through experience | Learn by doing | Use any initiative for value creation as a learning opportunity · Learn with others, including peers and mentors · Reflect and learn from both success and failure (your own and other people's) |

The numbering has no meaning: "the order in which they are presented does not imply a sequence in the acquisition process or a hierarchy" (p. 11).

## Eight levels (Table 2, p. 16)

| Level | | Progression | Autonomy and responsibility |
|---|---|---|---|
| Foundation | 1 Discover | Relying on support from others | Under direct supervision. |
| | 2 Explore | | With reduced support from others, some autonomy and together with my peers. |
| Intermediate | 3 Experiment | Building independence | On my own and together with my peers. |
| | 4 Dare | | Taking and sharing some responsibilities. |
| Advanced | 5 Improve | Taking responsibility | With some guidance and together with others. |
| | 6 Reinforce | | Taking responsibility for making decisions and working with others. |
| Expert | 7 Expand | Driving transformation, innovation and growth | Taking responsibility for contributing to complex developments in a specific field. |
| | 8 Transform | | Contributing substantially to the development of a specific field. |

The full model has **442 learning outcomes** ("I can…" statements) in 60 threads. They are in [`data/entrecomp-learning-outcomes.csv`](../data/entrecomp-learning-outcomes.csv), one row per outcome, with competence, thread, level and page. Example, 1.1 Spotting opportunities: level 1 "I can find opportunities to help others."; level 4 "I can proactively look for opportunities to create value, including out of necessity."; level 8 "I can spot and quickly take advantage of an opportunity." (p. 23)

## How this vault uses it

The authors are clear about limits: the learning outcomes "should not be taken as normative statements … or be used to measure student performance" (p. 17), and the framework is "a starting point. It must be tailored to the context of use" (p. 14). So:

1. **Tags are evidence.** A note in `mind/` may carry `entrecomp: [1.1, 3.3]` when the work shows those competences. The agent suggests; the student decides.
2. **The dashboard counts evidence per competence** and shows which ones have none yet. It never computes a score or a level.
3. **Levels are for self-assessment** in the weekly reflection, with the evidence links next to them ("I think I'm at 3 Experiment on 3.3 because of [[test-48h-repair]]"). The learning outcomes CSV gives the wording for each level.

### Which practice exercises which competences

This mapping is my design, not the JRC's. It sets the default tags in the note templates.

| Practice | Competences it usually shows | Why (descriptor it matches) |
|---|---|---|
| Play | 1.1, 1.2, 1.3, 3.3 | "Establish new connections and bring together scattered elements"; a hypothesis is a decision made "when the information available is partial" |
| Empathy | 1.4, 1.5, 3.4 | "Judge what value is in social, cultural and economic terms"; "Network" |
| Creation | 1.2, 2.3, 2.5, 3.1 | "Make the most of limited resources"; "Inspire and enthuse relevant stakeholders" |
| Experimentation | 2.4, 3.2, 3.3, 3.5 | "include structured ways of testing ideas and prototypes from the early stages" |
| Reflection | 2.1, 2.2, 3.5 | "Reflect on your needs, aspirations and wants"; "Reflect and learn from both success and failure" |
