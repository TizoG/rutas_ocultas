"use client";

import { SignInButton, SignedIn, SignedOut, UserButton } from "@clerk/nextjs";

export function NavAuth() {
  return (
    <div className="flex items-center gap-3">
      <SignedOut>
        <SignInButton mode="modal">
          <button className="rounded-full bg-lime-400 px-4 py-2 text-sm font-semibold text-slate-900">
            Iniciar sesión
          </button>
        </SignInButton>
      </SignedOut>
      <SignedIn>
        <UserButton afterSignOutUrl="/" />
      </SignedIn>
    </div>
  );
}
