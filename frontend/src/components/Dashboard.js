// 📁 qa-insight-frontend/src/components/Dashboard.js

import React, { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import axios from "axios";
import "chart.js/auto";

export default function Dashboard() {
  const [artifacts, setArtifacts] = useState([]);
  const [prDescription, setPrDescription] = useState("");
  const [bugSummary, setBugSummary] = useState("");
  const [suggestions, setSuggestions] = useState("");
  const [selectedRunId, setSelectedRunId] = useState("");

  // Fetch artifacts (filtered by run_id if selected)
  useEffect(() => {
    const url = selectedRunId
      ? `http://localhost:8000/artifacts?run_id=${selectedRunId}`
      : `http://localhost:8000/artifacts`;

    axios.get(url).then((res) => {
      const validArtifacts = res.data.filter(
        (a) => a.test_name && a.test_name.trim() !== ""
      );
      console.log("✅ Filtered Artifacts:", validArtifacts);
      setArtifacts(validArtifacts);
    });
  }, [selectedRunId]);

  const testNames = [...new Set(artifacts.map((a) => a.test_name))];

  const passCounts = testNames.map(
    (name) =>
      artifacts.filter((a) => a.test_name === name && a.status === "pass")
        .length
  );
  const failCounts = testNames.map(
    (name) =>
      artifacts.filter((a) => a.test_name === name && a.status === "fail")
        .length
  );

  const flakyTests = testNames
    .map((name) => {
      const failCount = artifacts.filter(
        (a) => a.test_name === name && a.status === "fail"
      ).length;
      return { name, failCount };
    })
    .filter((t) => t.failCount > 0)
    .sort((a, b) => b.failCount - a.failCount);

  const data = {
    labels: testNames,
    datasets: [
      {
        label: "Pass",
        backgroundColor: "#4caf50",
        data: passCounts,
      },
      {
        label: "Fail",
        backgroundColor: "#f44336",
        data: failCounts,
      },
    ],
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post("http://localhost:8000/suggest", {
      pr_description: prDescription,
      bug_summary: bugSummary,
    });
    setSuggestions(res.data.suggestions);
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">🧪 QA Insight Dashboard</h1>

      {/* Run ID Dropdown */}
      <div className="mb-4">
        <label className="font-medium mr-2">📊 Filter by Run ID:</label>
        <select
          className="border p-2"
          value={selectedRunId}
          onChange={(e) => setSelectedRunId(e.target.value)}
        >
          <option value="">All Runs</option>
          {[...new Set(artifacts.map((a) => a.run_id))].map((runId, idx) => (
            <option key={idx} value={runId}>
              {runId}
            </option>
          ))}
        </select>
      </div>

      <Bar data={data} />

      <div className="mt-8">
        <h2 className="text-lg font-semibold mb-2">🔥 Flaky Test Leaderboard</h2>
        <table className="min-w-full border border-gray-300 mb-8">
          <thead>
            <tr className="bg-gray-100">
              <th className="border px-4 py-2 text-left">Test Name</th>
              <th className="border px-4 py-2 text-left">Fail Count</th>
            </tr>
          </thead>
          <tbody>
            {flakyTests.map((test, index) => (
              <tr key={index}>
                <td className="border px-4 py-2">{test.name}</td>
                <td className="border px-4 py-2">{test.failCount}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="mt-8">
        <h2 className="text-lg font-semibold mb-2">🧠 Generate AI Test Suggestions</h2>
        <form onSubmit={handleSubmit} className="space-y-2">
          <textarea
            className="w-full border p-2"
            rows="3"
            placeholder="Enter PR description..."
            value={prDescription}
            onChange={(e) => setPrDescription(e.target.value)}
          />
          <textarea
            className="w-full border p-2"
            rows="2"
            placeholder="Optional bug summary..."
            value={bugSummary}
            onChange={(e) => setBugSummary(e.target.value)}
          />
          <button className="bg-blue-600 text-white px-4 py-2 rounded">
            Generate
          </button>
        </form>
        {suggestions && (
          <div className="mt-4 bg-gray-100 p-4 rounded">
            <h3 className="font-medium">💡 Suggested Test Scenarios:</h3>
            <pre className="whitespace-pre-wrap mt-2">{suggestions}</pre>
          </div>
        )}
      </div>
    </div>
  );
}
