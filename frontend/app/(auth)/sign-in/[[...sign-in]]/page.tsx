import { SignUp } from '@clerk/nextjs'

export default function SignUpPage() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-gray-50">
      <div className="mb-6 text-center">
        <h1 className="text-2xl font-semibold text-gray-900">PaperMind</h1>
        <p className="text-sm text-gray-500 mt-1">
          Create your account to get started
        </p>
      </div>
      <SignUp />
    </main>
  )
}