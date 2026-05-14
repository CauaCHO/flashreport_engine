
class ReportGenerator:
    def generate(self, context, entities, normalized):
        blocks = []

        problems = context.get("problems", [])
        actions = context.get("actions", [])
        results = context.get("results", [])

        # Casos especiais
        if "PROBLEMA_LOCAL_DISPOSITIVO" in problems or "FALHA_TERCEIRO" in problems:
            app_text = ", ".join(entities.get("apps", [])) if entities.get("apps") else "aplicativo/equipamento utilizado pelo cliente"
            blocks.append(f"Ao chegarmos ao local, o cliente relatou instabilidade relacionada a {app_text}.")
            blocks.append("Durante os testes realizados, foi verificado que a conexão funcionava normalmente em outros dispositivos, indicando falha localizada no dispositivo, aplicativo ou serviço utilizado pelo cliente.")
            blocks.append("Não foi constatada falha geral na conexão de internet, sendo o cliente orientado sobre a possível relação do problema com serviço ou equipamento de terceiros.")
            return "\n\n".join(blocks)

        # Introdução
        if "SEM_CONEXAO" in problems:
            blocks.append("Ao chegarmos ao local, foi identificado que o cliente estava sem conexão.")
        elif "LENTIDAO" in problems or "INSTABILIDADE" in problems:
            blocks.append("Ao chegarmos ao local, o cliente relatou instabilidade ou baixo desempenho na conexão.")
        elif "SINAL_BAIXO" in problems or "LINK_LOSS" in problems:
            blocks.append("Ao realizarmos a verificação técnica, foi identificado problema relacionado ao sinal da fibra.")
        elif "WIFI_RUIM" in problems:
            blocks.append("Ao chegarmos ao local, foi identificada baixa qualidade no sinal Wi-Fi no ambiente.")
        elif "CLIENTE_AUSENTE" in problems:
            blocks.append("Ao chegarmos ao local, não foi possível realizar o atendimento devido à ausência do cliente ou responsável.")

        # Ações
        if "INTERVENCAO_CTO" in actions:
            blocks.append("Realizada verificação na CTO para análise do ponto de atendimento relacionado à conexão do cliente.")
        if "SUBSTITUICAO_CONECTOR" in actions:
            blocks.append("Realizada a substituição/refação do conector óptico.")
        if "SUBSTITUICAO_ROTEADOR" in actions:
            blocks.append("Realizada a substituição do roteador.")
        if "SUBSTITUICAO_ONU" in actions:
            blocks.append("Realizada a substituição da ONU.")
        if "ALTERACAO_CANAL_WIFI" in actions:
            blocks.append("Realizada a alteração dos canais da rede Wi-Fi visando melhorar a estabilidade da conexão.")
        if "MEDICAO_SINAL" in actions:
            signal = entities.get("signal")
            if signal:
                blocks.append(f"Realizada medição de sinal óptico, constatando {signal['value']} dBm, indicando {signal['status']}.")
            else:
                blocks.append("Realizada medição de sinal óptico para validação da conexão.")
        if "RECONFIGURACAO" in actions:
            blocks.append("Realizada a reconfiguração do equipamento conforme necessidade técnica.")
        if "DIAGNOSTICO_COMPARATIVO" in actions:
            blocks.append("Realizado diagnóstico comparativo entre dispositivos para isolar a origem da falha.")

        # Resultado
        if "NORMALIZADO" in results:
            blocks.append("Após os procedimentos realizados, o funcionamento da internet foi normalizado no local.")
        elif "INTERNET_OK" in results:
            blocks.append("Durante os testes realizados, não foi constatada falha geral na conexão de internet.")
        elif "PENDENTE" in results:
            blocks.append("Atendimento permaneceu pendente, sendo necessário retorno para continuidade da tratativa.")

        if not blocks:
            blocks.append("Foi registrado atendimento técnico conforme informações repassadas pelo técnico.")
            blocks.append(f"Descrição informada: {normalized}.")
            blocks.append("Recomenda-se complementar o relatório com problema identificado, procedimento realizado e resultado final.")

        # remove duplicados
        unique = []
        for b in blocks:
            if b not in unique:
                unique.append(b)

        return "\n\n".join(unique)
