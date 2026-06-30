# Database Security Reference

## Supabase — Row Level Security (RLS)

### Enable RLS on every table
```sql
-- Run in Supabase SQL Editor
ALTER TABLE your_table ENABLE ROW LEVEL SECURITY;

-- Allow users to only see their own rows
CREATE POLICY "Users can view own data" ON your_table
  FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own data" ON your_table
  FOR INSERT WITH CHECK (auth.uid() = user_id);
```

### Check which tables have RLS disabled
```sql
SELECT tablename, rowsecurity
FROM pg_tables
WHERE schemaname = 'public' AND rowsecurity = false;
```

## Neon — Connection Security
- Use connection pooling (PgBouncer) for serverless environments
- Rotate passwords regularly via Neon dashboard → Branch → Edit
- Use separate database roles for read-only vs read-write operations

## Environment Variables — Best Practices

### What goes in .env (server-side only)
```
DATABASE_URL=postgresql://...
SUPABASE_SERVICE_ROLE_KEY=...  # Never expose this to the client
ANTHROPIC_API_KEY=...
CLERK_SECRET_KEY=...
```

### What's safe for client-side (NEXT_PUBLIC_ prefix)
```
NEXT_PUBLIC_SUPABASE_URL=...
NEXT_PUBLIC_SUPABASE_ANON_KEY=...  # Anon key only — RLS must be enforced
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=...
```

### Git Safety
- Add `.env` and `.env.local` to `.gitignore` immediately
- Run `git log --all -- .env` to check if secrets were ever committed
- If secrets were committed: rotate all credentials immediately, rewrite git history

## Common Mistakes
- Using the Supabase service role key on the client side (bypasses RLS entirely)
- Storing DATABASE_URL in a client-accessible location
- Not enabling RLS before going public
