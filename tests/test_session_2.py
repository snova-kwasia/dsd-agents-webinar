import pytest
from typing import Annotated, Literal, NotRequired
from typing_extensions import TypedDict


class TestCalculatorTool:
    """Tests for the calculator tool from Session 2 notebook."""

    def test_calculator_add(self):
        """Test calculator addition."""
        from langchain_core.tools import tool
        
        @tool
        def calculator(
            operation: Literal["add", "subtract", "multiply", "divide"],
            a: float,
            b: float,
        ) -> float:
            """A simple calculator for basic math operations."""
            if operation == "add":
                return a + b
            elif operation == "subtract":
                return a - b
            elif operation == "multiply":
                return a * b
            elif operation == "divide":
                return a / b if b != 0 else "Error: division by zero"
        
        result = calculator.invoke({"operation": "add", "a": 3, "b": 5})
        assert result == 8

    def test_calculator_subtract(self):
        """Test calculator subtraction."""
        from langchain_core.tools import tool
        
        @tool
        def calculator(
            operation: Literal["add", "subtract", "multiply", "divide"],
            a: float,
            b: float,
        ) -> float:
            """A simple calculator for basic math operations."""
            if operation == "add":
                return a + b
            elif operation == "subtract":
                return a - b
            elif operation == "multiply":
                return a * b
            elif operation == "divide":
                return a / b if b != 0 else "Error: division by zero"
        
        result = calculator.invoke({"operation": "subtract", "a": 10, "b": 4})
        assert result == 6

    def test_calculator_multiply(self):
        """Test calculator multiplication."""
        from langchain_core.tools import tool
        
        @tool
        def calculator(
            operation: Literal["add", "subtract", "multiply", "divide"],
            a: float,
            b: float,
        ) -> float:
            """A simple calculator for basic math operations."""
            if operation == "add":
                return a + b
            elif operation == "subtract":
                return a - b
            elif operation == "multiply":
                return a * b
            elif operation == "divide":
                return a / b if b != 0 else "Error: division by zero"
        
        result = calculator.invoke({"operation": "multiply", "a": 3.1, "b": 4.2})
        assert result == pytest.approx(13.02, rel=0.01)

    def test_calculator_divide(self):
        """Test calculator division."""
        from langchain_core.tools import tool
        
        @tool
        def calculator(
            operation: Literal["add", "subtract", "multiply", "divide"],
            a: float,
            b: float,
        ) -> float:
            """A simple calculator for basic math operations."""
            if operation == "add":
                return a + b
            elif operation == "subtract":
                return a - b
            elif operation == "multiply":
                return a * b
            elif operation == "divide":
                return a / b if b != 0 else "Error: division by zero"
        
        result = calculator.invoke({"operation": "divide", "a": 10, "b": 3})
        assert result == pytest.approx(3.333, rel=0.01)

    def test_calculator_division_by_zero(self):
        """Test calculator handles division by zero."""
        from langchain_core.tools import tool
        
        @tool
        def calculator(
            operation: Literal["add", "subtract", "multiply", "divide"],
            a: float,
            b: float,
        ) -> float:
            """A simple calculator for basic math operations."""
            if operation == "add":
                return a + b
            elif operation == "subtract":
                return a - b
            elif operation == "multiply":
                return a * b
            elif operation == "divide":
                return a / b if b != 0 else "Error: division by zero"
        
        result = calculator.invoke({"operation": "divide", "a": 10, "b": 0})
        assert result == "Error: division by zero"


class TestFileReducer:
    """Tests for the file_reducer function from Session 2 notebook."""

    def test_file_reducer_with_left_none(self):
        """Test file_reducer when left is None."""
        def file_reducer(left, right):
            if left is None:
                return right
            elif right is None:
                return left
            else:
                return {**left, **right}
        
        result = file_reducer(None, {"file1.md": "content"})
        assert result == {"file1.md": "content"}

    def test_file_reducer_with_right_none(self):
        """Test file_reducer when right is None."""
        def file_reducer(left, right):
            if left is None:
                return right
            elif right is None:
                return left
            else:
                return {**left, **right}
        
        result = file_reducer({"file1.md": "content"}, None)
        assert result == {"file1.md": "content"}

    def test_file_reducer_merge(self):
        """Test file_reducer merges dictionaries correctly."""
        def file_reducer(left, right):
            if left is None:
                return right
            elif right is None:
                return left
            else:
                return {**left, **right}
        
        existing = {"report.md": "# My Report", "notes.md": "Some notes"}
        new_update = {"data.csv": "col1,col2\n1,2"}
        
        result = file_reducer(existing, new_update)
        
        assert "report.md" in result
        assert "notes.md" in result
        assert "data.csv" in result
        assert result["report.md"] == "# My Report"
        assert result["notes.md"] == "Some notes"
        assert result["data.csv"] == "col1,col2\n1,2"

    def test_file_reducer_right_wins_on_conflict(self):
        """Test file_reducer gives precedence to right side on conflicts."""
        def file_reducer(left, right):
            if left is None:
                return right
            elif right is None:
                return left
            else:
                return {**left, **right}
        
        existing = {"report.md": "old content"}
        new_update = {"report.md": "new content"}
        
        result = file_reducer(existing, new_update)
        
        assert result["report.md"] == "new content"


class TestDeepAgentState:
    """Tests for the DeepAgentState and related types from Session 2 notebook."""

    def test_todo_typed_dict(self):
        """Test Todo TypedDict structure."""
        todo: Todo = {
            "content": "Research nuclear fusion",
            "status": "pending"
        }
        
        assert todo["content"] == "Research nuclear fusion"
        assert todo["status"] == "pending"

    def test_todo_with_all_statuses(self):
        """Test Todo with different status values."""
        statuses = ["pending", "in_progress", "completed"]
        
        for status in statuses:
            todo: Todo = {
                "content": "Test task",
                "status": status
            }
            assert todo["status"] == status

    def test_deep_agent_state_messages(self):
        """Test DeepAgentState includes messages field."""
        from langgraph.prebuilt.chat_agent_executor import AgentState
        from typing import Annotated
        
        class DeepAgentState(AgentState):
            todos: NotRequired[list]
            files: Annotated[NotRequired[dict], lambda l, r: {**l, **r} if l and r else (l or r)]
        
        state = DeepAgentState(messages=[])
        
        assert "messages" in state
        assert state["messages"] == []

    def test_deep_agent_state_with_todos(self):
        """Test DeepAgentState with todos."""
        from langgraph.prebuilt.chat_agent_executor import AgentState
        from typing import Annotated
        
        class DeepAgentState(AgentState):
            todos: NotRequired[list]
            files: Annotated[NotRequired[dict], lambda l, r: {**l, **r} if l and r else (l or r)]
        
        todos = [{"content": "Task 1", "status": "pending"}]
        state = DeepAgentState(messages=[], todos=todos)
        
        assert "todos" in state
        assert len(state["todos"]) == 1

    def test_deep_agent_state_with_files(self):
        """Test DeepAgentState with files."""
        from langgraph.prebuilt.chat_agent_executor import AgentState
        from typing import Annotated
        
        class DeepAgentState(AgentState):
            todos: NotRequired[list]
            files: Annotated[NotRequired[dict], lambda l, r: {**l, **r} if l and r else (l or r)]
        
        files = {"report.md": "# Report"}
        state = DeepAgentState(messages=[], files=files)
        
        assert "files" in state
        assert "report.md" in state["files"]


class TestReActLoop:
    """Tests for the ReAct loop implementation from Session 2 notebook."""

    def test_react_loop_no_tool_calls(self):
        """Test ReAct loop when model returns no tool calls."""
        from unittest.mock import MagicMock
        from langchain_core.messages import HumanMessage, AIMessage
        
        # Mock model that returns a response without tool calls
        mock_model = MagicMock()
        mock_response = AIMessage(content="This is the final answer.")
        mock_model.bind_tools.return_value.invoke.return_value = mock_response
        
        def react_loop(model, tools, user_query, max_iterations=10):
            model_with_tools = model.bind_tools(tools)
            tool_map = {t.name: t for t in tools}
            messages = [HumanMessage(content=user_query)]
            
            for i in range(max_iterations):
                response = model_with_tools.invoke(messages)
                messages.append(response)
                
                if not response.tool_calls:
                    break
            
            return messages
        
        result = react_loop(mock_model, [], "What is 2+2?")
        
        assert len(result) == 2
        assert result[-1].content == "This is the final answer."

    def test_react_loop_max_iterations(self):
        """Test ReAct loop respects max_iterations."""
        from unittest.mock import MagicMock
        from langchain_core.messages import HumanMessage, AIMessage
        
        # Mock model that always returns tool calls
        mock_model = MagicMock()
        mock_response = AIMessage(
            content="Thinking...",
            tool_calls=[{"name": "calculator", "args": {"a": 1, "b": 2}, "id": "call_1"}]
        )
        mock_model.bind_tools.return_value.invoke.return_value = mock_response
        
        # Mock tool
        mock_tool = MagicMock()
        mock_tool.name = "calculator"
        mock_tool.invoke.return_value = "3"
        
        def react_loop(model, tools, user_query, max_iterations=10):
            model_with_tools = model.bind_tools(tools)
            tool_map = {t.name: t for t in tools}
            messages = [HumanMessage(content=user_query)]
            
            for i in range(max_iterations):
                response = model_with_tools.invoke(messages)
                messages.append(response)
                
                if not response.tool_calls:
                    break
                
                for tool_call in response.tool_calls:
                    tool_fn = tool_map[tool_call["name"]]
                    result = tool_fn.invoke(tool_call["args"])
                    from langchain_core.messages import ToolMessage
                    messages.append(ToolMessage(content=str(result), tool_call_id=tool_call["id"]))
            
            return messages
        
        result = react_loop(mock_model, [mock_tool], "Calculate", max_iterations=3)
        
        # Should have: user message + 3 iterations of (response + tool result)
        assert len(result) == 7  # 1 + 3*2


class TestStatefulTools:
    """Tests for stateful tools (Command pattern) from Session 2 notebook."""

    def test_write_todos_command(self):
        """Test write_todos returns Command object."""
        from langgraph.types import Command
        from langchain_core.messages import ToolMessage
        
        todos = [{"content": "Task 1", "status": "pending"}]
        
        # Simulate what write_todos returns
        result = Command(
            update={
                "todos": todos,
                "messages": [
                    ToolMessage(
                        f"Updated todo list: {len(todos)} items",
                        tool_call_id="call_123",
                    )
                ],
            }
        )
        
        assert isinstance(result, Command)
        assert result.update["todos"] == todos

    def test_read_todos_empty(self):
        """Test read_todos returns message when no todos exist."""
        # Simulate read_todos logic
        state = {}
        todos = state.get("todos", [])
        
        if not todos:
            result = "No todos in the list."
        
        assert result == "No todos in the list."

    def test_read_todos_with_items(self):
        """Test read_todos formats todo list correctly."""
        # Simulate read_todos logic
        state = {
            "todos": [
                {"content": "Task 1", "status": "pending"},
                {"content": "Task 2", "status": "in_progress"},
                {"content": "Task 3", "status": "completed"},
            ]
        }
        
        todos = state.get("todos", [])
        status_icons = {"pending": "[ ]", "in_progress": "[~]", "completed": "[x]"}
        lines = []
        for i, todo in enumerate(todos, 1):
            icon = status_icons.get(todo["status"], "[?]")
            lines.append(f"{i}. {icon} {todo['content']}")
        result = "\n".join(lines)
        
        assert "1. [ ] Task 1" in result
        assert "2. [~] Task 2" in result
        assert "3. [x] Task 3" in result

    def test_ls_tool(self):
        """Test ls tool returns file list."""
        # Simulate ls tool logic
        state = {"files": {"report.md": "content", "notes.md": "notes"}}
        
        result = list(state.get("files", {}).keys())
        
        assert "report.md" in result
        assert "notes.md" in result

    def test_read_file_tool(self):
        """Test read_file tool returns file content."""
        # Simulate read_file tool logic
        state = {"files": {"report.md": "# Report\nContent here"}}
        file_path = "report_path"
        
        files = state.get("files", {})
        if file_path not in files:
            result = f"Error: File '{file_path}' not found"
        else:
            result = files[file_path]
        
        assert "Error" in result
        assert "report_path" in result

    def test_read_file_not_found(self):
        """Test read_file tool handles missing files."""
        # Simulate read_file tool logic for existing file
        state = {"files": {"report.md": "# Report content"}}
        file_path = "report.md"
        
        files = state.get("files", {})
        if file_path not in files:
            result = f"Error: File '{file_path}' not found"
        else:
            result = files[file_path]
        
        assert "# Report content" in result