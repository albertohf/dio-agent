# Fundamentos de segurança

Conceitos que o agente usa na skill `vulnerability-analysis`.

## Vulnerabilidade, ameaça e risco

- **Vulnerabilidade:** uma fraqueza num sistema (um código, uma configuração, um hábito). Exemplo: consulta SQL montada juntando texto digitado pela pessoa.
- **Ameaça:** algo ou alguém que pode explorar a fraqueza. Exemplo: uma pessoa mal-intencionada, um malware.
- **Risco:** a chance de a ameaça explorar a vulnerabilidade, combinada com o dano causado. Sem ameaça ou sem impacto, o risco é baixo; com os dois, é alto.
- **Exploração:** o uso real da vulnerabilidade para obter algo que não deveria ser possível.

Analogia: a porta sem tranca é a vulnerabilidade, o ladrão é a ameaça e a chance de ser roubado, somada ao prejuízo, é o risco.

## A tríade CIA

| Pilar | Significa | Exemplo de quebra |
|-------|-----------|-------------------|
| **Confidencialidade** | só quem tem permissão acessa | vazamento de senhas |
| **Integridade** | o dado não é alterado sem autorização | alterar o saldo de uma conta |
| **Disponibilidade** | o sistema funciona quando necessário | serviço fora do ar |

Toda análise deve dizer qual pilar foi afetado.

## Avaliando o risco

- **Impacto:** o dano se a falha for explorada.
- **Probabilidade:** a facilidade e a chance de alguém explorar (exposição, necessidade de acesso, complexidade).
- **Severidade:** combinação de impacto e probabilidade (baixa, média, alta, crítica).

Sempre justifique pelo contexto: onde roda, quem acessa, o que protege.

## Boas práticas

- **Validar e tratar toda entrada** do usuário; nunca confiar nela.
- **Consultas parametrizadas** em vez de montar SQL com texto concatenado (previne SQL Injection).
- **Menor privilégio:** cada conta e serviço com só o acesso necessário.
- **Defesa em profundidade:** várias camadas, para que uma falha não derrube tudo.
- **Segredos fora do código** (variáveis de ambiente, cofre de segredos); nunca em repositório.
- **Senhas com hash forte e salt** (bcrypt, argon2), nunca em texto puro.
- **Manter sistemas atualizados** e remover o que não é usado.
- **Registrar logs** de eventos sensíveis, sem gravar dados secretos.
- **Expor o mínimo** na internet: fechar portas e serviços desnecessários.

## Referências

- MITRE ATT&CK: https://attack.mitre.org (táticas e técnicas de ataque, para nomear o que foi observado)
- OWASP Top 10: https://owasp.org/www-project-top-ten (principais riscos de aplicações web)
