export const WHATSAPP_LINKS = {
  online: "https://wa.me/5512997932353?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20uma%20consulta%20online",
  taubate: "https://wa.me/5512991601313?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20uma%20consulta%20com%20a%20Dra.%20Victoria%20Feroldi",
  campos: "https://wa.me/5512996583276?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20uma%20consulta%20com%20a%20Dra.%20Victoria%20Feroldi%20em%20Campos%20do%20Jord%C3%A3o",
};

export const DOCTOR_INFO = {
  name: "Dra. Victoria Nunes Feroldi",
  shortName: "Victoria Nunes Feroldi",
  titleBadge: "Médica pós-graduada em psiquiatria",
  titleDescription: "Médica com pós-graduação em psiquiatria",
  crm: "CRM-SP 246645",
  email: "dravictoriaferoldi@gmail.com",
  phoneRaw: "5512997932353",
  phoneDisplay: "(12) 99793-2353",
  whatsappUrl: WHATSAPP_LINKS.online,
  emergencyNotice:
    "Em caso de emergência, procure um pronto-socorro ou ligue 192 (SAMU). Para apoio emocional imediato, ligue 188 (CVV).",
  disclaimer:
    "Este site tem caráter informativo e não substitui consulta médica. Em caso de emergência, procure um pronto-socorro ou ligue 192 (SAMU). Para apoio emocional imediato, ligue 188 (CVV).",
};

export const LOCATIONS = [
  { id: "online", name: "Consulta Online", badge: "Particular", highlight: "Telemedicina", schedule: "Quartas-feiras, das 8h às 12h", locationDetail: "Consulta por videochamada em ambiente reservado", actionLabel: "Agendar Consulta Online", whatsappUrl: WHATSAPP_LINKS.online, phoneDisplay: "(12) 99793-2353", icon: "online" },
  { id: "taubate", name: "Taubaté", badge: "Particular e Convênios", highlight: "Clínica Fator Humano", schedule: "Segunda e quinta, das 8h às 17h | Sexta, das 8h às 14h", locationDetail: "Rua Cel. Gomes Nogueira, 66, Centro, Taubaté - SP, CEP 12010-120", actionLabel: "Agendar em Taubaté (Fator Humano)", whatsappUrl: WHATSAPP_LINKS.taubate, phoneDisplay: "(12) 99160-1313", icon: "location" },
  { id: "campos", name: "Campos do Jordão", badge: "Particular", highlight: "Clínica Dermedical", schedule: "Horários informados pela equipe no agendamento", locationDetail: "Endereço informado pela equipe no ato do agendamento", actionLabel: "Agendar em Campos do Jordão", whatsappUrl: WHATSAPP_LINKS.campos, phoneDisplay: "(12) 99658-3276", icon: "location" },
];

export const FAQS = [
  { question: "A partir de qual idade posso agendar uma consulta?", answer: "O atendimento é destinado a pessoas a partir dos 16 anos, presencialmente ou on-line." },
  { question: "Como funciona a primeira consulta e o acompanhamento?", answer: "Na primeira consulta, a doutora procura conhecer sua história, seu contexto de vida, os sintomas e os tratamentos anteriores. A partir da avaliação, conversa com você sobre o tratamento, incluindo psicoterapia e medicação quando indicada. Os retornos costumam ser mensais, com intervalos ajustados conforme sua evolução e necessidade." },
  { question: "Qual a diferença entre psicólogo e médica com pós-graduação em psiquiatria?", answer: "O psicólogo é graduado em Psicologia e atua principalmente por meio de psicoterapias. A médica com pós-graduação em psiquiatria possui formação em Medicina e realiza avaliação médica, podendo indicar condutas clínicas e medicamentos quando apropriado. Os cuidados podem ser complementares." },
  { question: "Como funciona a consulta online por telemedicina?", answer: "A consulta é realizada por videochamada, em ambiente reservado e com orientações para acesso enviadas pela equipe. A modalidade online é particular e está disponível às quartas-feiras, das 8h às 12h." },
  { question: "Como escolher o WhatsApp correto para marcar minha consulta?", answer: "Escolha o card correspondente à modalidade e cidade desejadas na seção Locais e Canais de Agendamento. Cada botão direciona você ao canal específico da equipe responsável." },
  { question: "Posso renovar receitas ou pedir atestados pelo WhatsApp?", answer: "Não. Receitas, atestados e relatórios médicos são fornecidos exclusivamente durante a consulta, após avaliação médica. Não há emissão desses documentos pelo WhatsApp." },
  { question: "O canal atende casos de urgência?", answer: "Não. O WhatsApp é um canal administrativo e de agendamento, não de urgência ou emergência. Procure um pronto-socorro ou ligue 192 (SAMU). Para apoio emocional imediato, ligue 188 (CVV)." },
];
