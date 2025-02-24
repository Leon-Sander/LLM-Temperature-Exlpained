# Understanding Temperature in Language Models

## What is Temperature in Language Models?

Temperature is a **hyperparameter** used in language models to control the **randomness** of generated text. It modifies the probability distribution over possible next tokens before sampling, affecting how deterministic or diverse the output is.

- **Low Temperature (T < 1)** → More deterministic, higher probability tokens are chosen more often.
- **High Temperature (T > 1)** → More random, lower probability tokens have a greater chance of being selected.
- **Temperature = 0** → The model always picks the highest probability token (greedy decoding).

## How Temperature Works in Softmax
The softmax function converts model logits (raw scores) into probabilities:

$P(i) = \frac{e^{z_i / T}}{\sum_j e^{z_j / T}}$


Where:
- \( z_i \) is the logit for token \( i \)
- \( T \) is the temperature value
- Lower \( T \) makes high-probability tokens even more likely.
- Higher \( T \) flattens the distribution, making token selection more diverse.

## Example Calculation
Given logits:
\[ [2.0, 1.0, -0.5, -2.0, -3.0] \]

For **T = 1**:

| Token   | Logits  | e^Logits  | Probability |
|---------|---------|-----------|------------|
| Cinema  |  2.0    | 7.3891    | 0.6780     |
| Museum  |  1.0    | 2.7183    | 0.2494     |
| Stadium | -0.5    | 0.6065    | 0.0557     |
| School  | -2.0    | 0.1353    | 0.0124     |
| Test    | -3.0    | 0.0498    | 0.0046     |

For **T = 0.5**, probabilities become more skewed towards high-logit tokens, whereas for **T = 2.0**, the distribution flattens, making lower-logit tokens more likely.

## Conclusion
Adjusting the temperature allows fine-tuning of a model’s output to be **more deterministic** (low T) or **more creative** (high T), making it a crucial parameter in natural language generation tasks.

