import { UserButton } from '@clerk/nextjs'
import { auth } from '@clerk/nextjs/server'

export default async function DashboardPage() {
  const { userId } = await auth()

  return (
    <main className="min-h-screen p-8 bg-gray-50">
      <div className="max-w-4xl mx-auto">

        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-2xl font-semibold text-gray-900">PaperMind</h1>
            <p className="text-sm text-gray-500">
              AI document intelligence for legal &amp; finance
            </p>
          </div>
          {/* afterSignOutUrl removed — use signOutUrl instead in Clerk v6 */}
          <UserButton />
        </div>

        <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-6">
          <p className="text-green-800 text-sm font-medium">
            Phase 1 complete — authenticated successfully!
          </p>
          <p className="text-green-600 text-xs mt-1 font-mono">
            user_id: {userId}
          </p>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div className="border border-dashed border-gray-200 rounded-lg p-6 text-center bg-white">
            <p className="text-gray-400 text-sm font-medium">Document dashboard</p>
            <p className="text-gray-300 text-xs mt-1">Coming in Phase 2</p>
          </div>
          <div className="border border-dashed border-gray-200 rounded-lg p-6 text-center bg-white">
            <p className="text-gray-400 text-sm font-medium">Chat interface</p>
            <p className="text-gray-300 text-xs mt-1">Coming in Phase 4</p>
          </div>
        </div>

      </div>
    </main>
  )
}