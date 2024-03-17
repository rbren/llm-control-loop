def run_loop(agent, max_iterations=100):
    for i in range(max_iterations):
        print("STEP", i)
        action = agent.get_next_action()
        print(action)
        print("---")
        out = agent.maybe_perform_latest_action()
        if out and len(out) > 1000:
            out = out[:1000] + "..."
        print(out)
        print("==============")


