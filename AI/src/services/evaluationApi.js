
import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 30000,
});

export const submitEvaluation = async (evaluationData) => {
  const response = await api.post("/api/evaluate", evaluationData);
  return response.data;
};

export default api;
