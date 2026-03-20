export default function ChatPage({ params }: { params: { docId: string } }) {
  return (
    <main className="min-h-screen p-8 bg-gray-50">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-2xl font-semibold text-gray-900 mb-2">Chat</h1>
        <p className="text-sm text-gray-400 font-mono">doc_id: {params.docId}</p>
        <p className="text-sm text-gray-400 mt-2">Coming in Phase 4</p>
      </div>
    </main>
  )
}