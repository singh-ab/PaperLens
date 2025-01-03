import React, { useState, ChangeEvent, KeyboardEvent } from "react";
import Logo from "./components/Logo";
import { CirclePlus, LoaderCircle, SendHorizonalIcon } from "lucide-react";
import classNames from "classnames";
import axios from "axios";
import toast from "react-hot-toast";

const messages: string[] = [];

const API_URL = "http://localhost:8000";

const App: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [text, setText] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>("");
  const [pdfId, setPDFId] = useState<string | null>(null);

  // Handle file selection
  const handleFileChange = (e: ChangeEvent<HTMLInputElement>): void => {
    setError("");
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      if (selectedFile.type === "application/pdf") {
        setFile(selectedFile);
      } else {
        setFile(null);
        setError("Only PDF files are allowed.");
      }
    }
  };

  // Handle text input change
  const handleTextChange = (e: ChangeEvent<HTMLInputElement>): void => {
    setText(e.target.value);
  };

  // Upload PDF file
  const fileUploadHandler = async () => {
    if (!file) return;

    setLoading(true);
    try {
      const formData = new FormData();
      formData.append("file", file);

      const { data } = await axios.post(`${API_URL}/upload`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setPDFId(data.id);
      toast.success(data.message);
    } catch {
      toast.error("Failed to upload");
      setFile(null);
    } finally {
      setLoading(false);
      setText("");
    }
  };

  // Generate answer based on input text
  const generateAnswerHandler = async () => {
    if (!pdfId || !text) return;

    setLoading(true);
    try {
      const { data } = await axios.post(`${API_URL}/ask`, {
        text_id: pdfId,
        question: text,
      });

      messages.push(text, data.answer);
      toast.success("Answer generated");
      setText("");
    } catch {
      toast.error("Failed to generate");
    } finally {
      setLoading(false);
    }
  };

  // Handle Enter key press for submitting question
  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>): void => {
    if (e.key === "Enter") generateAnswerHandler();
  };

  // Render messages
  const renderMessages = () => {
    return messages.map((message, index) => (
      <div key={index} className={classNames("my-8 rounded w-6/7 p-3")}>
        <div className="text-slate-600">
          <span className="flex gap-4">
            <div
              className={classNames(
                "text-zinc-900 text-xl font-semibold rounded-full h-10 w-10 p-3 flex items-center justify-center",
                {
                  "bg-purple-400": index % 2 === 0,
                  "bg-green-400": index % 2 !== 0,
                }
              )}
            >
              {index % 2 === 0 ? "M" : "ai"}
            </div>
            <p>{message}</p>
          </span>
        </div>
      </div>
    ));
  };

  return (
    <main className="h-screen flex flex-col justify-between">
      <nav className="flex justify-between items-center p-3 h-16 shadow">
        <Logo />
        {!file ? (
          <div>
            <input
              className="block text-sm text-slate-500 md:file:mr-4 w-52 md:w-auto file:py-2 md:file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-pink-50 file:text-pink-700 hover:file:bg-pink-100"
              type="file"
              accept="application/pdf"
              onChange={handleFileChange}
            />
            {error && (
              <div className="text-xs text-right text-red-600">{error}</div>
            )}
          </div>
        ) : pdfId ? (
          <div className="text-green-400 px-4">{file.name}</div>
        ) : loading ? (
          <span className="animate-spin mx-4 ">
            <LoaderCircle color="#808080" />
          </span>
        ) : (
          <button
            onClick={fileUploadHandler}
            className="border flex text-zinc-800 mx-4 rounded-md gap-3 px-4 py-2"
          >
            <CirclePlus />
            Upload PDF
          </button>
        )}
      </nav>

      <div className="h-full border rounded-md p-5 overflow-y-scroll">
        {renderMessages()}
      </div>

      <div
        className={classNames(
          "flex justify-between md:mx-28 mx-5 my-10 border-slate-300 bg-zinc-50 border h-12 p-2 rounded items-center",
          { "opacity-50": loading }
        )}
      >
        <input
          type="text"
          value={text}
          onChange={handleTextChange}
          className="focus:outline-none w-full px-4 bg-transparent"
          placeholder="Ask Question..."
          disabled={loading}
          onKeyDown={handleKeyDown}
        />
        {pdfId && loading ? (
          <span className="animate-spin mx-4 ">
            <LoaderCircle color="#808080" />
          </span>
        ) : (
          <button onClick={generateAnswerHandler}>
            <SendHorizonalIcon color="#808080" />
          </button>
        )}
      </div>
    </main>
  );
};

export default App;
